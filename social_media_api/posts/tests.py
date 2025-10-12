from django.test import TestCase

# Create your tests here.
# posts/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass')
        self.other = User.objects.create_user(username='user2', password='pass')
        self.client = APIClient()
        self.client.login(username='user1', password='pass')
        self.post = Post.objects.create(author=self.user, title='T1', content='C1')

    def test_create_post(self):
        url = reverse('post-list')
        data = {'title': 'New', 'content': 'Content'}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Post.objects.count(), 2)

    def test_update_not_owner(self):
        self.client.logout()
        self.client.login(username='user2', password='pass')
        url = reverse('post-detail', args=[self.post.id])
        resp = self.client.put(url, {'title': 'X', 'content': 'Y'})
        self.assertIn(resp.status_code, (403, 405))  # permission denied

class CommentsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass')
        self.client = APIClient()
        self.client.login(username='user1', password='pass')
        self.post = Post.objects.create(author=self.user, title='T1', content='C1')

    def test_add_comment(self):
        url = reverse('comment-list')
        resp = self.client.post(url, {'post': self.post.id, 'content': 'Nice!'})
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(self.post.comments.count(), 1)
