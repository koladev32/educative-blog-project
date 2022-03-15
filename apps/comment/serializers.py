from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.abstract.serializers import AbstractSerializer
from apps.comment.models import Comment
from apps.article.models import Article
from apps.user.models import User


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    article = serializers.SlugRelatedField(queryset=Article.objects.all(), slug_field='public_id')

    # def validate_author(self, value):
    #     if self.context["request"].user != value:
    #         raise ValidationError("You can't create a comment for another user.")
    #     return value

    def validate_article(self, value):
        if self.instance:
            return self.instance.post
        return value

    class Meta:
        model = Comment
        # List of all the fields that can be included in a request or a response
        fields = ['id', 'article', 'author', 'body', 'created', 'updated']