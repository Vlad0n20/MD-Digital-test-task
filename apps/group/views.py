from apps.viewsets import CustomModelViewSet

from .models import Team
from . import serializers


class TeamViewSet(CustomModelViewSet):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamListSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.TeamCreateSerializer
        elif self.action == 'retrieve':
            return serializers.TeamDetailSerializer
        return super().get_serializer_class()
