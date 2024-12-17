from django.db import models

# 3 типа наследования: абстрактное, классическое и прокси

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
class Tag(models.Model):
    name = models.CharField(max_length=32,
                            unique=True)
    def __str__(self):
        return self.name

class Post(TimeStamp):
    name = models.CharField(max_length=32,
                            unique=True)
    text = models.TextField()
    # create = models.DateTimeField(auto_now_add=True) # Удалено благодаря наследованию от TimeStamp
    # update = models.DateTimeField(auto_now=True) # Удалено благодаря наследованию от TimeStamp
    # Связь с категорией
    # Один ко многому
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Связь с тегом (много к многому, вот так просто)
    tags = models.ManyToManyField(Tag)

    # Картинки
    # 2 варианта хранения картинки: в базе и в файле
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.name

# Классическое наследование
class CoreObject(models.Model):
    name = models.CharField(max_length=32)

class Car(CoreObject):
    description = models.TextField()

class Toy(CoreObject):
    text = models.TextField()