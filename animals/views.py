from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login


from .forms import *
from .models import *
from .utils import *


class AnimalsHome(DataMixin, ListView):  # отвечает за главную страницу
    model = Animals  # отображение моделей Animals
    template_name = "animals/index.html"
    context_object_name = "posts"  # index.html

    def get_context_data(self, object_list=None, **kwargs):  # динамический контекст
        context = super().get_context_data(
            **kwargs
        )  # получаем распаковку готового словаря
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):  # отображение конкретрых записей
        return Animals.objects.filter(time_published=True)


class AddPage(
    DataMixin,
    CreateView,
    LoginRequiredMixin,
):
    form_class = AddPostForm
    template_name = "animals/add_page.html"
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("home")

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(
    DataMixin, DetailView
):  # содержит объект, наД которым работает представление
    model = Animals
    template_name = "animals/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"])
        return dict(list(context.items()) + list(c_def.items()))


class AnimalsCategory(DataMixin, ListView):  # страница, представляющая список объектов
    model = Animals
    template_name = "animals/index.html"
    context_object_name = "posts"
    allow_empty = False  # 404 if not slug category

    def get_queryset(self):
        return Animals.objects.filter(
            cat__slug=self.kwargs["cat_slug"], time_published=True
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Категория - " + str(context["posts"][0].cat)
        context["menu"] = menu
        context["cat_selected"] = context["posts"][0].cat_id
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "animals/register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):  # валидация при регистрации и авторизация 2 in 1
        user = form.save()
        login(self.request, user)
        return redirect("home")


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "animals/login.html"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):  # валидация формы и реверс
        return reverse_lazy("home")


def logout_user(request):  # выйти и вернуться на авторизацию
    logout(request)
    return redirect("login")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена</h1>")


def contact(request):
    return HttpResponse("Обратная связь")


def about(request):
    return render(request, "animals/about.html", {"menu": menu, "title": "О сайте"})
