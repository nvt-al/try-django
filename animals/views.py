from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения Animals")


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