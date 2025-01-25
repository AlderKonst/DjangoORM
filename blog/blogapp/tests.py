from django.test import TestCase
from faker import Faker
from mixer.backend.django import mixer

from .models import Post, Category
from usersapp.models import BlogUser

class PostTestCase(TestCase):

    ''' 1. Вариант, где всё вручную
    def test_has_image(self):
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username='test_user', email='test@test', password='password000')
        post = Post.objects.create(name='test_post', text='some', user=user, category=category)
        self.assertFalse(post.has_image()) # assertFalse - возвращает ли False

    def test_some_method(self):
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username='test_user', email='test@test', password='password000')
        post = Post.objects.create(name='test_post', text='some', user=user, category=category)
        self.assertFalse(post.some_method() == 'Неправильный текст в методе в class Post') # Возвращает ли False (правильный текст такой: 'Некоторый метод в class Post'
    '''

    # 2. Вариант, где всё через setUp
    def setUp(self):
        category = Category.objects.create(name='test_category')
        user = BlogUser.objects.create_user(username='test_user', email='test@test', password='password000')
        self.post = Post.objects.create(name='test_post', text='some', user=user, category=category)
        self.post_str = Post.objects.create(name='test_post_str', text='some', user=user, category=category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image()) # assertFalse - возвращает ли False

    def test_some_method(self):
        post = Post.objects.get(name='test_post') # Делаем так, если только уникальные имена (нерекомендуется так)
        self.assertFalse(post.some_method() == 'Неправильный текст в методе в class Post') # Возвращает ли False (правильный текст такой: 'Некоторый метод в class Post'

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category') # Проверяем, что строка корректна

# Варианты через генерацию данных
# faker (простые данные, н-ер, случайное имя, универсален и можно использовать где угодно использовать)
# FactoryBoy (данные для конкретной модели Django)
# mixer (чтобы полностью создать поддельную модель)
# 3 Вариант через faker
class PostTestCaseFaker(TestCase):
    def setUp(self):
        faker=Faker('ru_RU')
        category = Category.objects.create(name=faker.name())
        user = BlogUser.objects.create_user(username=faker.name(), email=faker.email(), password=faker.password())
        self.post = Post.objects.create(name=faker.name(), text=faker.name(), user=user, category=category)

        # print(f'{self.post.name}, {category.name}, {user.email}, {user.password[:10]}...')
        category = Category.objects.create(name='test_category') # Тут снова создаём из-за def test_str
        self.post_str = Post.objects.create(name='test_post_str', text='some', user=user, category=category)

    def test_has_image(self):
        self.assertFalse(self.post.has_image()) # assertFalse - возвращает ли False

    def test_some_method(self):
        self.assertFalse(self.post.some_method() == 'Неправильный текст в методе в class Post') # Возвращает ли False (правильный текст такой: 'Некоторый метод в class Post'

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category') # Проверяем, что строка корректна

# 4 Вариант через mixer
class PostTestCaseMixer(TestCase):
    def setUp(self):
        self.post = mixer.blend(Post)

        # Хороший вариант, создаёт даже юзера связанного с постом, т.е. с другими таблицами с другого приложения
        # category = mixer.blend(Category, name='test_category') #
        # self.post_str = mixer.blend(Post, name='test_post_str', category=category)
        # print(f'{self.post.name}, {self.post.category.name}, {self.post.user.email}, {self.post.user.password[:10]}...')

        # Лучший вариант
        self.post_str = mixer.blend(Post, name='test_post_str', category__name='test_category')

    def test_has_image(self):
        self.assertFalse(self.post.has_image()) # assertFalse - возвращает ли False

    def test_some_method(self):
        self.assertFalse(self.post.some_method() == 'Неправильный текст в методе в class Post') # Возвращает ли False (правильный текст такой: 'Некоторый метод в class Post'

    def test_str(self):
        self.assertEqual(str(self.post_str), 'test_post_str, category: test_category') # Проверяем, что строка корректна