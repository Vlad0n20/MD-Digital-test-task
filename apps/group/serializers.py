from rest_framework import serializers

from .models import Team
from apps.user.serializers import UserListSerializer


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'users',)


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name')


class TeamDetailSerializer(serializers.ModelSerializer):
    users = UserListSerializer(many=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'users')

