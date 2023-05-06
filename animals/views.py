from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render, redirect

from animals.models import *

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


def index(request):
    posts = Animals.objects.all()

    context = {
        "posts": posts,
        "menu": menu,
        "title": "Главная страница",
        "cat_selected": 0,
    }
    return render(request, "animals/index.html", context=context)


def about(request):
    return render(request, "animals/about.html", {"menu": menu, "title": "О сайте"})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    post = get_object_or_404(Animals, slug=post_slug)    # выбирает пост с ключом pk(получение конкретной записи из бд)
                                                         # если не находит, то вывод 404
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'animals/post.html', context=context)


def show_category(request, cat_slug):
    posts = Animals.objects.filter(cat__slug=cat_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        "posts": posts,
        "menu": menu,
        "title": "Отображение по категориям",
        "cat_selected": cat_slug,
    }
    return render(request, "animals/index.html", context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена</h1>")
