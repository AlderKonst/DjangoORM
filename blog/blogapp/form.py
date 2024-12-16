from django import forms
from .models import Post, Tag

class ContactForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    email = forms.EmailField(label='Электронный адрес', max_length=30)
    message = forms.CharField(label='Сообщение')

class  PostForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}))

    tags = forms.ModelMultipleChoiceField( # Чекбоксы
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Post # Инициируем модель, которая будет использоваться в форме
        # fields = '__all__' # Для загрузки всех полей модели таблицы Post
        # fields = ('name', 'text', 'category', 'image') # Для загрузки только нужных полей модели таблицы Post
        exclude = ('tags',) # То же самое, но через исключение каких-либо полей