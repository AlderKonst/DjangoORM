from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser

class RegistrationForm(UserCreationForm): # Тут есть двойное введение пароли и их проверка на идеинтичность
    class Meta:
        model = BlogUser
        fields = ('username', 'password1', 'password2', # Эти поля и так есть, стандартные
                  'email') # Если ещё нужен email (или ещё другие поля), то и его добавляем