from django.db.models import Count

from .models import Category


menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
]


class DataMixin:
    paginate_by = 10                                          # кол-во записей на странице 

    def get_user_context (self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('animals'))    # отображение категорий с >=1 постом

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:            # проверка на авторизацию 
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context