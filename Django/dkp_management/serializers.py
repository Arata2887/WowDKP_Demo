
from rest_framework import serializers
from .models import Player, DKPLog, EquipmentType, Raid, Boss, EventRule

class EventRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRule
        fields = ['id', 'name', 'points']  # 包括需要的字段

# Include existing serializers if present
