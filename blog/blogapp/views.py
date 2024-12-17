from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # Базовые классы
from django.views.generic.base import ContextMixin # Для создание общих классов

from .models import Post, Tag
from .form import ContactForm, PostForm
from django.core.mail import send_mail

def main_view(request):
    posts = Post.objects.all()
    return render(request,'blogapp/index.html', context={'posts': posts})

def contact_view(request):
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

def create_post(request):
    if request.method == 'GET':
        form = PostForm() # Из forms.py
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, # Передаём данные, которые сюда придут
                        files=request.FILES) # Если есть изображения или файлы, то ещё и это прописываем
        if form.is_valid(): # Если данные формы заполнены правильно
            form.save() # Все данные, поля помнит, поэтому их загрузит и заполнит в БД
            return HttpResponseRedirect(reverse('blogapp:index'))  # Перенаправляем на главную страницу
        else: # Если данные формы заполнены неправильно, то загрузит прежднюю страницу с формой для заполнения
            return render(request, 'blogapp/create.html', context={'form': form}) # причём в полях страницы уже будут видны ошибки

class NameContextMixin(ContextMixin): # Чтобы везде, где передадим класс NameContextMixin прописывало функции ниже
    def get_context_data(self, **kwargs): # Отвечает за передачу параметров в контекст (тот самый context)
        context = super().get_context_data(**kwargs)
        context['name'] = 'Тэги'
        return context

class TagListView(ListView, NameContextMixin):
    model =Tag
    tamplate_name = 'blogapp/tag_list.html' # Необязательно, если его не будет, то будет где-то храниться по-умолчанию
    context_object_name = 'tags' # Если хочется на странице использовать не стандартное object_list, а своё имя

    def get_queryset(self): # Получение данных (по-умолчанию возвращает все тэги, но можно настроить здесь ниже)
        return Tag.objects.all() # В таком виде обычно возвращает (по-умолчанию), а можно настроить (переопределить), например, на получение определённых данных

# Детальная информация
class TagDetailView(DetailView, NameContextMixin):
    model = Tag
    tamplate_name = 'blogapp/tag_detail.html'

    # Эти 3 функции сделаны так, что ничего не меняют, но в дальнейшем можно понастроить и изменить где надо, если не устраивают имена по-умолчанию
    def get(self, request, *args, **kwargs): # Базовый get-функция переопределения
        self.tag_id =kwargs['pk'] # Для переопределения имени поля ключа (демонстрируется в учебных целях)
        return super().get(request, *args, **kwargs) # Переопределяется
    def get_object(self, queryset=None): # Для получения одного объекта
        return get_object_or_404(Tag,
                                 pk=self.tag_id) # Имя поля ключа снова такая же (демонстрируется в учебных целях)


# Создание тэга
class TagCreateView(CreateView, NameContextMixin): # Вместо подобной громадной def create_post(request)
    model = Tag
    # form_class =
    fields = '__all__' # Выбираем все поля класса Tag
    success_url = reverse_lazy('blogapp:tag_list') # Вместо длинной конструкции с return HttpResponseRedirect(reverse('blogapp:tag_list.html'))
    template_name = 'blogapp/tag_create.html'
    def post(self, request, *args, **kwargs): # Срабатывает, когда пришёл POST-запрос
        return super().post(request, *args, **kwargs)

    def form_valid(self, form): # Метод срабатывает после того, как выясняется, что форма правильная
        # Кроме того, можно с этой формой тут делать всякое
        return super().form_valid(form)


class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('blogapp:tag_list')
    template_name = 'blogapp/tag_create.html'

class TagDelateView(DeleteView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('blogapp:tag_list')
    template_name = 'blogapp/tag_delate_confirm.html' # Страница подтверждения удаления