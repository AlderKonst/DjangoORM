from django.db import models
from django.contrib.auth.models import AbstractUser # Абстрактный, чтобы он не создавался в БД, наследовался для создания модели интерактивного добавления нового ползователя
from django.db.models.signals import post_save # Сигнал, который будет вызываться после создания пользователя
from django.dispatch import receiver

class BlogUser(AbstractUser): # Нужно в начале проекта всегда его создавать, чтобы была возможность изменения работы с пользователями и не пришлось проблемно пересоздавать БД после того, как сделали своего пользователя
    # pass # Если будет только pass, то будут те же стандартные поля и неуникальный email
    email = models.EmailField(unique=True) # Теперь email уникальный
    is_author = models.BooleanField(default=False) # Автор поста или нет

    ''' Использование save
    def save(self, *args, **kwargs): #  Переопределяем метод сохранения нового пользователя
        super().save(*args, **kwargs)  # Сохраняем пользователя
        if not Profile.objects.filter(user=self).exists(): # Если профиль не существует
            Profile.objects.create(user=self) # То создаем профиль
    '''

class Profile(models.Model): # При создании нового пользователя будет создаваться профиль Profile
    info = models.TextField(blank=True)
    user = models.OneToOneField(BlogUser, on_delete=models.CASCADE)

@receiver(post_save, sender=BlogUser) # Сигнал, который будет вызываться после создания пользователя
def create_profile(sender, instance, **kwargs): # Функция, которая будет вызываться после создания пользователя
    print('Сработал обработчик сигнала')
    if not Profile.objects.filter(user=instance).exists(): # Если профиль не существует
        Profile.objects.create(user=instance) # То создаем профиль