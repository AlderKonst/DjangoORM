from django.db import models
from django.contrib.auth.models import AbstractUser # Абстрактный, чтобы он не создавался в БД, наследовался для создания модели интерактивного добавления нового ползователя

class BlogUser(AbstractUser): # Нужно в начале проекта всегда его создавать, чтобы была возможность изменения работы с пользователями и не пришлось проблемно пересоздавать БД после того, как сделали своего пользователя
    # pass # Если будет только pass, то будут те же стандартные поля и неуникальный email
    email = models.EmailField(unique=True) # Теперь email уникальный
    is_author = models.BooleanField(default=False) # Автор поста или нет