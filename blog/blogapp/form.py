from django import forms
from .models import Post, Tag

class ContactForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    email = forms.EmailField(label='Электронный адрес', max_length=30)
    message = forms.CharField(label='Сообщение')

class PostForm(forms.ModelForm): # Определение формы на основе модели Post
    name = forms.CharField( # Поле для ввода названия поста
        label='Название', # Метка для поля ввода
        widget=forms.TextInput( # Использование текстового поля для ввода
            attrs={'placeholder': 'Имя', 'class': 'form-control'})) # Атрибуты для текстового поля: плейсхолдер и класс CSS

    tags = forms.ModelMultipleChoiceField( # Чекбоксы для выбора нескольких тегов
        queryset=Tag.objects.all(), # Получение всех объектов Tag из базы данных
        widget=forms.CheckboxSelectMultiple()) # Использование виджета для отображения чекбоксов
    class Meta:
        model = Post # Инициируем модель, которая будет использоваться в форме
        # fields = '__all__' # Для загрузки всех полей модели таблицы Post
        # fields = ('name', 'text', 'category', 'image') # Для загрузки только нужных полей модели таблицы Post
        exclude = ('tags',) # То же самое, но через исключение каких-либо полей