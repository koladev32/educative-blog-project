from django.http.response import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from apps.comment.models import Comment
from apps.comment.serializers import CommentSerializer
from apps.authentication.permissions import UserPermission


class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()

        article_pk = self.kwargs['article_pk']
        if article_pk is None:
            return Http404
        queryset = Comment.objects.filter(article__public_id=article_pk)

        return queryset

    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])

        self.check_object_permissions(self.request, obj)

        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


