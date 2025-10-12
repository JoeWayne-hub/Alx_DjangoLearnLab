from django.test import TestCase

# Create your tests here.
# posts/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like
from notifications.models import Notification

User = get_user_model()

class LikeNotificationTest(APITestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='u1', password='p')
        self.u2 = User.objects.create_user(username='u2', password='p')
        self.post = Post.objects.create(author=self.u2, title='T', content='C')
        self.client.login(username='u1', password='p')

    def test_like_creates_notification(self):
        url = reverse('post-like', args=[self.post.id])
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(Like.objects.filter(post=self.post, user=self.u1).exists())
        self.assertTrue(Notification.objects.filter(recipient=self.u2, actor=self.u1, verb__icontains='liked').exists())

    def test_unlike_removes(self):
        self.client.post(reverse('post-like', args=[self.post.id]))
        resp = self.client.post(reverse('post-unlike', args=[self.post.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Like.objects.filter(post=self.post, user=self.u1).exists())

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
