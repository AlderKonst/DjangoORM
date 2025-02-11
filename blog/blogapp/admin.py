from django.contrib import admin
from .models import Category, Post, Tag

admin.site.register(Category)

def clear_rating(modeladmin, request, queryset): # Очистка рейтинга
    queryset.update(rating=1)
clear_rating.short_description = 'Очистить рейтинг до 1'

def set_active(modeladmin, request, queryset): # Сделать активным
    queryset.update(is_active=True)
set_active.short_description = 'Активировать'

class PostAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['id', 'name', 'text', 'category', 'tags_on_admin', 'rating', 'is_active'] # Поля в виде колонок с возможностью сортировки
    actions = [clear_rating, set_active]

admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['name', 'is_active'] # Поля в виде колонок с возможностью сортировки
    actions = [set_active]

admin.site.register(Tag, TagAdmin)