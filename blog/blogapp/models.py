from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16,
                            unique=True)
    description = models.TextField(blank=True)
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

class Post(models.Model):
    name = models.CharField(max_length=32,
                            unique=True)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Связь с категорией
    # Один ко многому
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Связь с тегом (много к многому, вот так просто)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name