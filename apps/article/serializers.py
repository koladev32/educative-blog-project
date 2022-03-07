from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.abstract.serializers import AbstractSerializer
from apps.article.models import Article
from apps.user.models import User


class ArticleSerializer(AbstractSerializer):
    
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='public_id',
    )
    
    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create an article for another user.")
        return value
    
    class Meta: 
        model = Article
        fields = ['id', 'title', 'body', 'author', 'created', 'updated']