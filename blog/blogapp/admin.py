from django.contrib import admin
from .models import Category, Post, Tag

class PostAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['name', 'text', 'category'] # Поля в виде колонок с возможностью сортировки

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)