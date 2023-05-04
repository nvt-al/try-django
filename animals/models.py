from django.db import models
from django.urls import reverse


class Animals(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    time_published = models.BooleanField(default=True)
    cat = models.ForeignKey(
        "Category", on_delete=models.PROTECT, null=True
    )  # связь Many to One
    # запрещает удалять категории, на которые есть ссылки из модели

    def __str__(self):
        return self.title

    # генерация ссылок на объекты из бд
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})


# модель Category, которая представляет категории животных
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})
