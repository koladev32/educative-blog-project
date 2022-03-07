from django.db import models

from apps.abstract.models import AbstractModel, AbstractManager


class ArticleManager(AbstractManager):
    pass

class Article(AbstractModel):
    author = models.ForeignKey('apps_user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    objects = ArticleManager()

    class Meta:
        db_table = 'article'