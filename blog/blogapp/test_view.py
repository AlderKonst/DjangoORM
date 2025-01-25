from django.contrib.auth.decorators import login_required
from django.test import Client
from django.test import TestCase
from faker import Faker
from usersapp.models import BlogUser


class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        response = self.client.get('/') # Проверяем, что главная страница открывается
        self.assertEqual(response.status_code, 200) # А это значит, что код ответа должен быть 200
        response = self.client.get('/contact/')  # Теперь также проверяем, что страница c контактами открывается
        self.assertEqual(response.status_code, 200)

        # Теперь post-запрос
        response = self.client.post('/contact/',# Проверяем, что отправляются данные формы контактов
                                   {'name': self.fake.name(),
                                         'email': self.fake.email(),
                                         'message': self.fake.text()})
        self.assertEqual(response.status_code, 302) # Если отправились данные правильно, то код ответа должен быть 302 (редирект)

        # Проверяем передаются ли данные в контексте
        response = self.client.get('/')
        self.assertTrue('posts' in response.context) # Есть ли в контексте словарь 'posts'

    # Если пользователь незалогинился, то статус должен быть 302 (поскольку редирект на логин-пароль происходит)
    # Если же залогинился, то статус должен быть 200
    def test_login_required(self):
        BlogUser.objects.create_user(username='test_user', email='test@test', password='password000')
        # Если не вошёл в систему, то 302
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)
        # Если вошёл в систему, то 200
        self.client.login(username='test_user', password='password000')
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)