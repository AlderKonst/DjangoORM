from django.urls import path, include
from .models import Category, Post, Tag
from rest_framework import routers, serializers, viewsets

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
    # Так много запросов, нужно в api_views.py ещё использовать prefetch_related
    tags = serializers.StringRelatedField(many=True) # Связанный объект будет показывать в виде строки
    #tags = serializers.HyperlinkedRelatedField( # Связанный объект будет показывать в виде api-ссылок (рекомендуемый метод)
    #    many=True, read_only=True, view_name='tag_detail') # Но не работает у меня почему-то!!!
    class Meta:
        model = Post
        exclude = ['user'] # Кроме этого поля

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'