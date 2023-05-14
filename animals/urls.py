from django.urls import path

from .views import *

# .as_view() класс представления, который обратаывает запросы

# cache_page(60)(AnimalsHome.as_view()) кэширует результаты представления на 60 секунд.
# Это означает, что при первом запросе к этой странице,
# результаты будут сохранены в кэше на 60 секунд, и при последующих 
# запросах в течение этого времени, результаты будут возвращены из кэша,
urlpatterns = [
    path("", AnimalsHome.as_view(), name="home"),
    path("about/", about, name="about"),
    path("addpage/", AddPage.as_view(), name="add_page"),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("post/<slug:post_slug>/", ShowPost.as_view(), name="post"),
    path("category/<slug:cat_slug>/", AnimalsCategory.as_view(), name="category"),
]
