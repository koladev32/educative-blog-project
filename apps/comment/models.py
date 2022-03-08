from django.db import models

from apps.abstract.models import AbstractManager, AbstractModel


class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    author = models.ForeignKey('apps_user.User', on_delete=models.CASCADE)
    article = models.ForeignKey('apps_article.Article', on_delete=models.CASCADE)
    body = models.TextField()

    objects = CommentManager()