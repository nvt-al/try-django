from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from animals.models  import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Animals.objects.all()
    return render(request, "animals/index.html", {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, "animals/about.html", {'menu': menu, 'title': 'О сайте'})


def categories(request, categories_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1> Категории </h1><p>{categories_id}</p>")


def archive(reques, year):
    if int(year) > 2020:
        return redirect("home", permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1></p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> Страница не найдена</h1>")
