from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class AnimalAdmin(admin.ModelAdmin):
    list_display = (  # visual list
        "id",
        "title",
        "time_create",
        "get_html_photo",
        "time_published",
    )
    list_display_links = ("id", "title")  # click fields
    search_fields = ("title", "content")
    list_editable = ("time_published",)
    list_filter = ("time_published", "time_create")
    prepopulated_fields = {"slug": ("title",)}  # auto slug
    fields = ('title', 'slug', 'cat', 'content', 'photo',  'time_published') # редактируемые поля 



    # отображение img вместо ссылок
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50")

    get_html_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)  # search category
    prepopulated_fields = {"slug": ("name",)}  # auto slug


admin.site.register(Animals, AnimalAdmin)
admin.site.register(Category, CategoryAdmin)


# admin.site.site_title = 'Админ-панель сайта о животных'
admin.site.site_header = "Админ-панель сайта о животных"
