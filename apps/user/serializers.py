from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('username', 'password',)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'is_active', 'is_staff', 'is_superuser')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'username': {'required': False},
        }