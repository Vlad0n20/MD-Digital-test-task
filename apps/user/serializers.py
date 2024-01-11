import re

from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.get('password'))
        return user

    def validate_first_name(self, value):
        special_characters_pattern = re.compile(r'[!@#$%^&*()_+{}|;":,.<>?/~`]')
        if special_characters_pattern.search(value):
            raise serializers.ValidationError("First name cannot contain special characters.")

        return value

    def validate(self, attrs):
        if User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError("User with this email already exists")
        return attrs

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',)


class UserDetailSerializer(serializers.ModelSerializer):
    joined_duration = serializers.SerializerMethodField()

    def get_joined_duration(self, obj) -> int:
        return (obj.date_joined - obj.last_login).days

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'is_active',
                  'is_staff', 'is_superuser', 'joined_duration')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                  'is_active', 'is_staff', 'is_superuser')
