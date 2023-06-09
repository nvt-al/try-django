from django.db import models
from django.urls import reverse


class Animals(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")     # slug - уникальная ссылка на страницу поста
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    time_published = models.BooleanField(default=True,verbose_name="Публикация")
    cat = models.ForeignKey("Category", on_delete=models.PROTECT,verbose_name="Категории")      # запрещает удалять категории, на которые есть ссылки из модели

    def __str__(self):
        return self.title

                                                                    # генерация ссылок на объекты из бд/ "смотреть на сайте в 'admin' "
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Необычные животные"
        verbose_name_plural = "Необычные животные"                   # delete "s" in name
        ordering = ["time_create", "title"]                          # sorting order



class Category(models.Model):                                                                 # модель Category, которая представляет категории животных
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")   # slug - уникальная ссылка на страницу категорий

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']