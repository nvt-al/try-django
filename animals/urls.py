from django.urls import path

from .views import *

urlpatterns = [
    path("", AnimalsHome.as_view(), name="home"),    # вызов функции
    path("about/", about, name="about"),
    path("addpage/", AddPage.as_view(), name="add_page"),
    path("contact/", contact, name="contact"),
    path("login/", login, name="login"),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name="post"),
    path("category/<slug:cat_slug>/", AnimalsCategory.as_view(), name="category"),
]
