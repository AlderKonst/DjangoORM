from django.test import TestCase
from .models import Post, Category
from usersapp.models import BlogUser

class PostTestCase(TestCase): # Вариант, где всё вручную
    def test_has_image(self):
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username='test_user', email='test@test', password='password000')
        post = Post.objects.create(name='test_post', text='some', user=user, category=category)
        self.assertFalse(post.has_image()) # assertFalse - возвращает ли False