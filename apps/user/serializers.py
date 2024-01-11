from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.get('password'))
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
        }


class UserListSerializer(serializers.ModelSerializer):

    def validate_username(self, value):
        if 'test' in value:
            raise serializers.ValidationError("Username cannot contain 'test'")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class UserDetailSerializer(serializers.ModelSerializer):
    joined_duration = serializers.SerializerMethodField()

    def get_joined_duration(self, obj) -> int:
        return (obj.date_joined - obj.last_login).days

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'joined_duration')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'username': {'required': False},
        }
