from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(username="user1")
        cls.post1 = Post.objects.create(
            title="sample_title_1",
            text="sample_text_1",
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user1)

        cls.post2 = Post.objects.create(
            title="sample_title_2",
            text="sample_text_2",
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user1)

    def test_post_model_str(self):
        self.assertEqual(self.post1.title, str(self.post1))

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_post_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_post_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail', args=[1000]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse("post_create"), {
            'title': 'sample_title_3',
            'text': 'sample_text_3',
            'author': self.user1.id,
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'sample_title_3')
        self.assertEqual(Post.objects.last().text, 'sample_text_3')

    def test_post_update_view(self):
        response = self.client.post(reverse("post_update", args=[self.post1.id]), {
            'title': 'sample_title_1_updated',
            'text': 'sample_text_1_updated',
            'author': self.user1.id,
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.get(pk=self.post1.id).title, 'sample_title_1_updated')
        self.assertEqual(Post.objects.get(pk=self.post1.id).text, 'sample_text_1_updated')

    def test_post_delete_view(self):
        response = self.client.post(reverse("post_delete", args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)