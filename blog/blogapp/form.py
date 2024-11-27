from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Название', max_length=100)
    email = forms.EmailField(label='Электронный адрес', max_length=30)
    message = forms.CharField(label='Сообщение')