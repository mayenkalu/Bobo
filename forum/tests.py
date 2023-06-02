from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Thread, Post, Comment
from django.contrib.auth import get_user_model
User = get_user_model()

class ForumTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')
        self.category = Category.objects.create(name='Test Category')
        self.thread = Thread.objects.create(title='Test Thread', created_by=self.user, category=self.category)
        self.post = Post.objects.create(message='Test Post', created_by=self.user, thread=self.thread)

    def test_category_list_view(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('forum:category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Category')

    def test_thread_list_view(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('forum:thread_list', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Thread')

    def test_thread_detail_view(self):
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('forum:thread_detail', args=[self.thread.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Thread')
        self.assertContains(response, 'Test Post')

    def test_thread_create_view(self):
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('forum:thread_create', args=[self.category.id]), {'title': 'New Thread', 'category': self.category.id})
        self.assertEqual(response.status_code, 302) # Checks for redirect after successful creation
        self.assertTrue(Thread.objects.filter(title='New Thread').exists())

    def test_post_create_view(self):
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('forum:post_create', args=[self.thread.id]), {'message': 'New Post'})
        self.assertEqual(response.status_code, 302) # Checks for redirect after successful creation
        self.assertTrue(Post.objects.filter(message='New Post').exists())

    def test_comment_create_view(self):
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('forum:comment_create', args=[self.post.id]), {'message': 'New Comment'})
        self.assertEqual(response.status_code, 302) # Checks for redirect after successful creation
        self.assertTrue(Comment.objects.filter(message='New Comment').exists())
