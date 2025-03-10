"""
Конфигурация URL для проекта блога.

Список urlpatterns перенаправляет URL-адреса на представления. Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
Примеры:
Функциональные представления
1. Добавьте импорт: from my_app import views
2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Классовые представления
1. Добавьте импорт: from other_app.views import Home
2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другой URLconf
1. Импортируйте функцию include(): from django.urls import include, path
2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""

from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('create/', views.create_post, name='create'),
    path('post/<int:id>/', views.post, name='post'),
    path('tag_list', views.TagListView.as_view(), name='tag_list'), # Так создаются маршруты с базовыми классами
    path('tag_detail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'), # pk - это первичный ключ
    path('tag_create/', views.TagCreateView.as_view(), name='tag_create'), #
    path('tag_update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'), #
    path('tag_delate/<int:pk>/', views.TagDeleteView.as_view(), name='tag_delate'), #
    path('category_detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'), #
    path('post_category_create/<int:pk>/', views.PostCategoryCreateView.as_view(), name='post_category_create'), #
    path('simple/', views.SimpleMainAjax.as_view(), name='simple_ajax'), # Страница с AJAX
]