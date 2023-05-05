from django import template
from animals.models import *

# Создаем объект Library из модуля template
register = template.Library()


# Регистрируем пользовательский тег с помощью декоратора simple_tag
# И определяем функцию get_categories, которая возвращает все объекты модели Category
# Мы также можем передать аргумент name, который будет использоваться в качестве имени тега
@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('animals/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, "cat_selected": cat_selected}
