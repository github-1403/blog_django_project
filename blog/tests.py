from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        self.post1 = Post.objects.create(
            title="sample_title_1",
            text="sample_text_1",
            status=Post.STATUS_CHOICES[0][0],
            author=user1)

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)
