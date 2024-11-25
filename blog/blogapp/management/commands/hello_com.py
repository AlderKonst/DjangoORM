from django.core.management.base import BaseCommand
# from blogapp.models import Question as Poll
from blogapp.models import Category, Post, Tag

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Выбираем все категории
        categories = Category.objects.all()
        print(categories)
        for i in categories:
            print(i)
        print('Конец')

        # Выбрать одну категорию
        category = Category.objects.get(name='Игрушки')
        print(category)

        # Выбрать несколько категорий
        category = Category.objects.filter(name="Игрушки")
        print(category)