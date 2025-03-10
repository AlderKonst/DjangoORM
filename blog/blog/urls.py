"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

from rest_framework import routers
from blogapp.api_views import CategoryViewSet, PostViewSet, TagViewSet

#router_categories = routers.DefaultRouter()
#router_categories.register(r'categories', CategoryViewSet)
#router_posts = routers.DefaultRouter()
#router_posts.register(r'posts', PostViewSet)
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         include(('blogapp.urls', 'blogapp'),
         namespace='blog')), # Это чтобы в index.html можно было сделать так: <a href="{% url 'blog:post' id=post.id %}">
    path('users/',
         include(('usersapp.urls', 'users'),
         namespace='users')),
    #path('api/v0/categories/', include(router_categories.urls)), # По категории через API
    #path('api/v0/posts/', include(router_posts.urls)), # По постам через API
    path('api/v0/', include(router.urls)), # По категории через API
    path('api-auth/',
         include('rest_framework.urls',
         namespace='rest_framework')) # Для работы с API
] + debug_toolbar_urls() # В отличие от старых версий Django, проще и добавляем не в блок "if settings.DEBUG"

if settings.DEBUG: # Чтобы изображения могли отображаться в браузере
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)