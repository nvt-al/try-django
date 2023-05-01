from django.urls import path

from .views import*

urlpatterns = [
    path("", index, name="home"),
    path("categories/<int:categories_id>/", categories),
    
]