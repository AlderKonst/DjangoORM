from django.core.management.base import BaseCommand
from mixer.backend.django import mixer
from blogapp.models import Category, Post, Tag
from usersapp.models import BlogUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        Post.objects.all().delete()
        Tag.objects.all().delete()
        Category.objects.all().delete()
        BlogUser.objects.filter(is_superuser=False).delete()
        count = 300
        for i in range(count):
            p = (i/count) * 100
            print(p, '%')
            mixer.blend(Post)
        print('Всё')