from django.test import TestCase

# Create your tests here.
# accounts/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from posts.models import Post


User = get_user_model()


class FeedTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='u1', password='p')
        self.user2 = User.objects.create_user(username='u2', password='p')
        self.post_by_u2 = Post.objects.create(author=self.user2, title='T', content='C')

    def test_feed_shows_followed_users_posts(self):
        self.client.login(username='u1', password='p')
        # u1 follows u2
        self.user1.following.add(self.user2)
        resp = self.client.get(reverse('feed'))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        # depending on serializer shape, check presence
        self.assertTrue(any(item['id'] == self.post_by_u2.id for item in data))

class FollowTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='u1', password='p')
        self.user2 = User.objects.create_user(username='u2', password='p')

    def test_follow_unfollow(self):
        self.client.login(username='u1', password='p')
        url = reverse('follow-toggle', args=[self.user2.id])
        # follow
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(self.user2 in self.user1.following.all())
        # unfollow
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(self.user2 in self.user1.following.all())
