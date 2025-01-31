from django.db import models
from usersapp.models import BlogUser

# 3 типа наследования: абстрактное, классическое и прокси

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)

class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=False)
    objects = models.Manager() # Чтобы objects (тот, что по-умолчанию) оставался работать как раньше
    active_objects = ActiveManager() # Переопределяем метод get_queryset
    class Meta:
        abstract = True

'''
class UpdatedObjectsMixin(models.Manager): # Чтобы дата обновления не была равна дате создания
    def get_queryset(self):
        all_objects = super().get_queryset() 
        return all_objects.filter(update=F('create') # Тут нужен F-запрос, однако будем его проходить позже
'''

class TimeStamp(models.Model): # Абстрактный тип наследования здесь
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Теперь для TimeStamp не создаётся новая таблица, чисто для избежания дублирования
    # Т.е. данные хранятся только в каждом наследнике

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16,
                            unique=True)
    description = models.TextField(blank=True)
    # create = models.DateTimeField(auto_now_add=True)
    # update = models.DateTimeField(auto_now=True)
    # Основные типы данных
    # Дата
    # models.DateField
    # models.DateTimeField
    # models.TimeField
    # # Числа
    # models.IntegerField
    # models.PositiveIntegerField
    # models.PositiveSmallIntegerField
    # models.FloatField
    # models.DecimalField
    # # Логический
    # models.BooleanField
    # # Байты
    # models.BinaryField
    # # Картинки
    # models.ImageField
    # # Файл
    # models.FileField
    # # url, email
    # models.URLField
    # models.EmailField
    def __str__(self):
        return self.name

class Tag(IsActiveMixin):
    name = models.CharField(max_length=32,
                            unique=True)
    def __str__(self):
        return self.name

class Post(TimeStamp, IsActiveMixin):
    name = models.CharField(max_length=32,
                            unique=True)
    text = models.TextField()
    # create = models.DateTimeField(auto_now_add=True) # Удалено благодаря наследованию от TimeStamp
    # update = models.DateTimeField(auto_now=True) # Удалено благодаря наследованию от TimeStamp
    # Связь с категорией
    # Один ко многому
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    # Связь с тегом (много к многому, вот так просто)
    tags = models.ManyToManyField(Tag)

    # Картинки
    # 2 варианта хранения картинки: в базе и в файле
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.name}, category: {self.category.name}'
    def has_image(self):
        return bool(self.image)

    def some_method(self):
        return 'Некоторый метод в class Post'
    def tags_on_admin(self): # Получение списка тегов
        tags = self.tags.all()
        return ', '.join([tag.name for tag in tags])

# Классическое наследование
class CoreObject(models.Model):
    name = models.CharField(max_length=32)

class Car(CoreObject):
    description = models.TextField()

class Toy(CoreObject):
    text = models.TextField()