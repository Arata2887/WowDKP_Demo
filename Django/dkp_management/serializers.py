# serializers.py

from rest_framework import serializers
from .models import Player, DKPLog, EventRule

# Player 序列化器
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'character_name', 'profession', 'role', 'specialization', 'total_dkp']

# DKPLog 序列化器
class DKPLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DKPLog
        fields = ['id', 'player', 'points', 'action_type', 'timestamp', 'note', 'raid', 'boss']

# EventRule 序列化器
class EventRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRule
        fields = ['id', 'name', 'points']
