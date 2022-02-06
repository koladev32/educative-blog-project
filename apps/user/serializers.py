from apps.abstract.serializers import AbstractSerializer
from apps.user.models import User


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'name', 'email', 'is_active',
                  'created', 'updated']
