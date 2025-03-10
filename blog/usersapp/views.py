from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import BlogUser
from django.urls import reverse_lazy, reverse
from rest_framework.authtoken.models import Token
from  django.shortcuts import HttpResponseRedirect
from django.http import JsonResponse

class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'

class UserCreateView(CreateView):
    model = BlogUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

class UserDetailView(DetailView): # Чтобы токен мог создать пользователь себе
    template_name = 'usersapp/profile.html'
    model = BlogUser

def update_token(request):
    user = request.user
    if user.auth_token: # Если уже токен есть, то обновляем его
        user.auth_token.delete()
        Token.objects.create(user=user)
    else: # Если же нет
        Token.objects.create(user=user) # то создаём
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))

def update_token_ajax(request): #  Обновление токена с помощью AJAX (кнопка ниже)
    user = request.user
    if user.auth_token: # Если уже токен есть, то обновляем его
        user.auth_token.delete()
        token = Token.objects.create(user=user)
    else: # Если же нет
        token = Token.objects.create(user=user) # то создаём
    return JsonResponse({'key': token.key}) # Передаём данные в виде AJAX