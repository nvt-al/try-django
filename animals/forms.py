from django import forms
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
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title



    


# формы, не связанные с models
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label="Заголовок")
#     slug = forms.SlugField(max_length=255, label="URL")
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={"cols": 60, "rows": 10}), label="Контент"
#     )  # виджет Textarea, который позволяет вводить многострочный текст и имеет размерность 60 столбцов и 10 строк
#     time_published = forms.BooleanField(
#         label="Публикация", required=False, initial=True
#     )  # initial - default value/checkbox true
#     cat = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         label="Выберите категорию",
#         empty_label="Категория не выбрана",
#     )  # Объект модели QuerySet>, из которого берутся варианты выбора для поля и который используется для проверки выбора пользователя
