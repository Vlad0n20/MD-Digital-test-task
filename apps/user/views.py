from apps.viewsets import CustomModelViewSet

from .models import User
from . import serializers


class UserViewSet(CustomModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.UserCreateSerializer
        elif self.action == 'retrieve':
            return serializers.UserDetailSerializer
        elif self.action == 'update':
            return serializers.UserUpdateSerializer
        return super().get_serializer_class()
