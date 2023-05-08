from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from .forms import *
from .models import *

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


class AnimalsHome(ListView):  # отвечает за главную страницу
    model = Animals  # отображение моделей Animals
    template_name = "animals/index.html"
    context_object_name = "posts"  # index.html

    def get_context_data(self, object_list=None, **kwargs):  # динамический контекст
        context = super().get_context_data(
            **kwargs
        )  # получаем распаковку готового словаря
        context["menu"] = menu
        context["title"] = "Главная страница"
        context["cat_selected"] = 0
        return context

    def get_queryset(self):  # отображение конкретрых записей
        return Animals.objects.filter(time_published=True)


# def index(request):
#     posts = Animals.objects.all()

#     context = {
#         "posts": posts,
#         "menu": menu,
#         "title": "Главная страница",
#         "cat_selected": 0,
#     }
#     return render(request, "animals/index.html", context=context)


def about(request):
    return render(request, "animals/about.html", {"menu": menu, "title": "О сайте"})


class AddPage(CreateView):  # представление, отображающее форму
    form_class = AddPostForm
    template_name = "animals/add_page.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавление статьи"
        context["menu"] = menu
        return context


# def addpage(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = AddPostForm()
#     return render(
#         request,
#         "animals/add_page.html",
#         {"form": form, "menu": menu, "title": "Добавление статьи"},
#     )


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DetailView):  # содержит объект, на которым работает представление
    model = Animals
    template_name = "animals/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["post"]
        context["menu"] = menu
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(
#         Animals, slug=post_slug
#     )  # выбирает пост с ключом pk(получение конкретной записи из бд)
#     # если не  находит, то вывод 404
#     context = {
#         "post": post,
#         "menu": menu,
#         "title": post.title,
#         "cat_selected": post.cat_id,
#     }
#     return render(request, "animals/post.html", context=context)


class AnimalsCategory(ListView):  # страница, представляющая список объектов
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


# def show_category(request, cat_slug):
#     posts = Animals.objects.filter(cat__slug=cat_slug)

#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         "posts": posts,
#         "menu": menu,
#         "title": "Отображение по категориям",
#         "cat_selected": cat_slug,
#     }
#     return render(request, "animals/index.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена</h1>")
