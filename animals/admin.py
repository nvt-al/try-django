from django.contrib import admin

from .models import *


class AnimalAdmin(admin.ModelAdmin):
    list_display = (                            # visual list
        "id", 
        "title", 
        "time_create", 
        "photo", 
        "time_published"
        )
    list_display_links = ("id", "title")        # click fields
    search_fields = ("title", "content")
    list_editable = ("time_published",)
    list_filter = ("time_published", "time_create")
    prepopulated_fields = {'slug': ('title',)}  # auto slug


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)                   # search category
    prepopulated_fields = {'slug': ('name',)}   # auto slug


admin.site.register(Animals, AnimalAdmin)
admin.site.register(Category, CategoryAdmin)
