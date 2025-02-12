from django.contrib import admin
from django.db.models import F

from .models import Category, Post, Tag

admin.site.register(Category)

def clear_rating(modeladmin, request, queryset): # Очистка рейтинга
    queryset.update(rating=1)
clear_rating.short_description = 'Очистить рейтинг до 1'

def set_active(modeladmin, request, queryset): # Сделать активным
    """
    for i in queryset: # Очень долго
        i.is_active=True
        i.save()
    """
    queryset.update(is_active=True)
set_active.short_description = 'Активировать'

def add_rating(modeladmin, request, queryset): # Увеличить рейтинг
    """
    for i in queryset: # Очень долго, делает много запросов
        i.rating += 1
        i.save()
    """
    queryset.update(rating=F('rating')+1) # Быстро, делает за раз
add_rating.short_description = 'Рейтинг+1'

class PostAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['id', 'name', 'text', 'category', 'tags_on_admin', 'rating', 'is_active'] # Поля в виде колонок с возможностью сортировки
    actions = [clear_rating, set_active, add_rating]

admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['name', 'is_active'] # Поля в виде колонок с возможностью сортировки
    actions = [set_active]

admin.site.register(Tag, TagAdmin)