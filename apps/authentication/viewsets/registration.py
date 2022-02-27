from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.serializers import RegistrationSerializer


class RegistrationViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be registered.
    """
    http_methods_names = ['post']
    permissions_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": tokens["refresh"],
            "token": tokens["access"]
        }, status=status.HTTP_201_CREATED)