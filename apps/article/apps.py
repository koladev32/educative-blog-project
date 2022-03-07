from cProfile import label
from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.article'
    label = 'apps_article'
