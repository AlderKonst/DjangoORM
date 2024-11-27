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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_view, name='index'),
    path('create/', views.create_post, name='create'),
    path('post/<int:id>/', views.post, name='post'),
    path('contacts/', views.contacts, name='contacts')
]

if settings.DEBUG: # Чтобы изображения могли отображаться в браузере
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)