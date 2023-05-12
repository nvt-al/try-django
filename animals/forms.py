from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError


from .models import *


# формы, связанные с models
class AddPostForm(forms.ModelForm):
    def __init__(
        self, *args, **kwargs
    ):  # конструктор класса, который вызывается при создании экземпляра класса формы.
        super().__init__(
            *args, **kwargs
        )  # вызов конструктора базового класса, который инициализирует форму
        self.fields["cat"].empty_label = "Категория не выбрана"

    class Meta:
        model = Animals
        fields = ["title", "slug", "content", "photo", "time_published", "cat"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 60, "rows": 10}),
        }

    def clean_title(self):  # пользовательская валидация
        title = self.cleaned_data["title"]
        if len(title) > 200:
            raise ValidationError("Длина превышает 200 символов")
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    email = forms.EmailField(
        label="Email", widget=forms.EmailInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    password2 = forms.CharField(
        label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    # позволяет настроить форму на основе модели, определить, какие поля будут 
    # отображаться в форме и как они будут отображаться.
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))