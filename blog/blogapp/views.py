from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .form import ContactForm
from django.core.mail import send_mail

def main_view(request):
    posts = Post.objects.all()
    return render(request,'blogapp/index.html', context={'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) # Получим данные из формы
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                'Тестовая отправка сообщения на емейл', # Тема письма
                f'Ваше сообщение\n{message}\nпринято', # Текст сообщения
                'koalder@koalder.ru', # Кому
                [email], # Cписок получателей
                fail_silently=True # Не выводить ошибки
            )
            return HttpResponseRedirect(reverse('blogapp:index')) # Перенаправляем на главную страницу
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'blogapp/create.html', context={'form': form})

def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post})

def contacts(request):
    return render(request, 'blogapp/contacts.html')