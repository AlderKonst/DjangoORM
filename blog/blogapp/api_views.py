from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication # Загружаем применяемые здесь методы авторизации по API
from .permissions import ReadOnly, IsAuthor
from .models import Category, Post, Tag
from .serializers import CategorySerializer, PostSerializer, TagSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly] # Доступ к изменению данных через API есть только у админа или только чтение
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsAuthor | ReadOnly] # Доступ к изменению данных через API есть у авторов (даже у админа нет без IsAdminUser) или только чтение
    queryset = Post.objects.prefetch_related('tags') # Это оптимизирует (минимизирует) число запросов (здесь с 104 до 5)
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication] # То, каким образом могут быть авторизованы по API, включая через токен
    permission_classes = [IsAuthenticated] # Любые авторизованные
    queryset = Tag.objects.all()
    serializer_class = TagSerializer