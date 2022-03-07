from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.article.serializers import ArticleSerializer
from apps.article.models import Article
from apps.authentication.permissions import UserPermission
class ArticleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    serializer_class = ArticleSerializer
    permission_classes = (UserPermission,)
    
    def get_queryset(self):
        return Article.objects.all()
    
    def get_object(self):
        obj = Article.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
