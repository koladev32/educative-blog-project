from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.article.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    serializer_class = ArticleSerializer
    permission_classes = ()
