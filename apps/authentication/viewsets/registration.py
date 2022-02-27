from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status

from apps.authentication.serializers import RegistrationSerializer


class RegistrationViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be registered.
    """
    http_methods_names = ['post']
    permissions_classes = (AllowAny,)
    serializer_class = RegistrationSerializer