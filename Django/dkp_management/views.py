
from rest_framework import viewsets
from .models import Player, DKPLog, EquipmentType, Raid, Boss, EventRule
from .serializers import PlayerSerializer, DKPLogSerializer, EventRuleSerializer

class EventRuleViewSet(viewsets.ModelViewSet):
    queryset = EventRule.objects.all()
    serializer_class = EventRuleSerializer

# Include existing viewsets if present
