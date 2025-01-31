from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.template.defaultfilters import title
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # Базовые классы
from django.views.generic.base import ContextMixin # Для создание общих классов
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Для постраничной навигации

from .models import Post, Tag
from .forms import ContactForm, PostForm

def main_view(request):
    posts = Post.active_objects.all() # Получаем все активные посты (вместо objects, ранее создал в models.py)
    paginator = Paginator(posts, 2) # Количество постов на странице
    page = request.GET.get('page') # Получаем номер страницы
    title_main = 'главная страница'
    # joke = 'Заходит мужик в баню ...'
    try: # Проверяем, есть ли посты на странице
        posts = paginator.page(page) # Если есть, то выводим посты на страницу
    except PageNotAnInteger: # Если страница не целое число, то выводим первые 2 поста
        posts = paginator.page(1) # Получаем первые 2 поста
    except EmptyPage: # Если страница пустая, число за пределами возможных страниц, то выводим последние 2 поста
        posts = paginator.page(paginator.num_pages) # Получаем последние 2 поста
    return render(request,'blogapp/index.html', context={'posts': posts, 'title_main': title_main})

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
            return HttpResponseRedirect(reverse('blog:index')) # Перенаправляем на главную страницу
        else:
            return render(request, 'blogapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'blogapp/contact.html', context={'form': form})

@user_passes_test(lambda u: u.is_superuser) # Теперь, при @user_passes_test смотреть пост разрешено только ползователям с определённым условием (здесь только админ)
def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post})

@login_required # Вот так просто добавляем это и посты смогут создавать только залогиненные пользователи
def create_post(request):
    if request.method == 'GET':
        form = PostForm() # Из forms.py
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, # Передаём данные, которые сюда придут
                        files=request.FILES) # Если есть изображения или файлы, то ещё и это прописываем
        if form.is_valid(): # Если данные формы заполнены правильно
            form.instance.user = request.user # Сохраняем в БД таблице текущего пользователя
            form.save() # Все данные, поля помнит, поэтому их загрузит и заполнит в БД
            return HttpResponseRedirect(reverse('blog:index'))  # Перенаправляем на главную страницу
        else: # Если данные формы заполнены неправильно, то загрузит прежднюю страницу с формой для заполнения
            return render(request, 'blogapp/create.html', context={'form': form}) # причём в полях страницы уже будут видны ошибки

class NameContextMixin(ContextMixin): # Чтобы везде, где передадим класс NameContextMixin прописывало функции ниже
    def get_context_data(self, **kwargs): # Отвечает за передачу параметров в контекст (тот самый context)
        context = super().get_context_data(**kwargs)
        context['name'] = 'Тэги'
        return context

class TagListView(ListView, NameContextMixin):
    model =Tag
    template_name = 'blogapp/tag_list.html' # Необязательно, если его не будет, то будет где-то храниться по-умолчанию
    context_object_name = 'tags' # Если хочется на странице использовать не стандартное object_list, а своё имя
    paginate_by = 2 # Количество постов на странице, т.е. гораздо короче

    def get_queryset(self): # Получение данных (по-умолчанию возвращает все тэги, но можно настроить здесь ниже)
        return Tag.active_objects.all() # В таком виде обычно возвращает (по-умолчанию), а можно настроить (переопределить), например, на получение определённых данных

# Детальная информация
class TagDetailView(LoginRequiredMixin, # Оказывается ещё и это нужно, чтобы был редирект (на занятиях не показали)
                    UserPassesTestMixin, # Для функциональности @user_passes_test, но в виде класса, однако условия разрешения нужно писать тут ниже в def test_func(self)
                    DetailView, NameContextMixin):
    model = Tag
    template_name = 'blogapp/tag_detail.html'
    login_url = settings.LOGIN_URL  # Используем значение из settings.py, чтобы редирект был (на занятиях не показали)

    def test_func(self): # См. выше про UserPassesTestMixin
        return self.request.user.is_superuser # Да, решение при использовании классов по-длиннее получается

    def dispatch(self, request, *args, **kwargs): # А также нужно вот так переопределить этот метод, чтобы был редирект при неподходящем логине (тоже в занятиях не показали)
        if not self.test_func():
            return redirect(self.login_url)  # Редирект на страницу входа
        return super().dispatch(request, *args, **kwargs)

    # Эти 3 функции сделаны так, что ничего не меняют, но в дальнейшем можно понастроить и изменить где надо, если не устраивают имена по-умолчанию
    def get(self, request, *args, **kwargs): # Базовый get-функция переопределения
        self.tag_id =kwargs['pk'] # Для переопределения имени поля ключа (демонстрируется в учебных целях)
        return super().get(request, *args, **kwargs) # Переопределяется
    def get_object(self, queryset=None): # Для получения одного объекта
        return get_object_or_404(Tag,
                                 pk=self.tag_id) # Имя поля ключа снова такая же (демонстрируется в учебных целях)

# Создание тэга
class TagCreateView(LoginRequiredMixin, # Чтобы теги мог создавать только залогиненный, !!! причём LoginRequiredMixin должен 1-м идти
                    CreateView, NameContextMixin): # Вместо подобной громадной def create_post(request)
    model = Tag
    # form_class =
    fields = '__all__' # Выбираем все поля класса Tag
    success_url = reverse_lazy('blog:tag_list') # Вместо длинной конструкции с return HttpResponseRedirect(reverse('blogapp:tag_list.html'))
    template_name = 'blogapp/tag_create.html'
    def post(self, request, *args, **kwargs): # Срабатывает, когда пришёл POST-запрос
        return super().post(request, *args, **kwargs)

    def form_valid(self, form): # Метод срабатывает после того, как выясняется, что форма правильная
        # Кроме того, можно с этой формой тут делать всякое
        # form.instance.user = self.request.user # Если в классах (для примера), то вот так сохраняем в таблице БД текущего пользователя
        return super().form_valid(form)


class TagUpdateView(UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'

class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_delate_confirm.html' # Страница подтверждения удаления