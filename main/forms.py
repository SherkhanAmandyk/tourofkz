from news.models import News
from .models import Register
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput, EmailField, forms


class NewsForms(ModelForm):
    class Meta:
        model = News
        fields = ['name', 'byName', 'byPhoto', 'dateTime', 'description', 'photo']

        widgets = {
            'name' : TextInput(attrs={
                'class' : 'form-control form-control-lg',
                'placeholder' : 'Название новости'
            }),
            'byName': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Ваше имя'
            }),
            'dateTime': DateTimeInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Дата публикации',
                'type': 'datetime-local'
            }),
            'description': Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Текст'
            })
        }



class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'surname', 'age', 'dateReg', 'email', 'country', 'city']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Имя'
            }),
            'surname': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Фамилия'
            }),
            'dateReg': DateInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Дата рождения',
                'type': 'datetime-local'
            }),
            'age': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Возраст'
            }),
            'email': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'E-mail'
            }),
            'country': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Страна'
            }),
            'city': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Город'
            })
        }