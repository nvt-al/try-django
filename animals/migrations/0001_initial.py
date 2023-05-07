# Generated by Django 4.2 on 2023-05-06 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="Категория"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Animals",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="URL"),
                ),
                ("content", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "photo",
                    models.ImageField(
                        upload_to="photos/%Y/%m/%d/", verbose_name="Фото"
                    ),
                ),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время добавления"
                    ),
                ),
                (
                    "time_update",
                    models.DateTimeField(auto_now=True, verbose_name="Время изменения"),
                ),
                (
                    "time_published",
                    models.BooleanField(default=True, verbose_name="Публикация"),
                ),
                (
                    "cat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="animals.category",
                        verbose_name="Категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Необычные животные",
                "verbose_name_plural": "Необычные животные",
                "ordering": ["time_create", "title"],
            },
        ),
    ]
