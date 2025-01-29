from django.contrib import admin
from .models import Category, Post, Tag

def clear_rating(modeladmin, request, queryset): # Очистка рейтинга
    queryset.update(rating=1)
clear_rating.short_description = 'Очистить рейтинг до 1'

class PostAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['name', 'text', 'category', 'tags_on_admin', 'rating'] # Поля в виде колонок с возможностью сортировки
    actions = [clear_rating]

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)