from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Player, DKPLog, EventRule
from .serializers import PlayerSerializer, DKPLogSerializer, EventRuleSerializer


# 定义 Player, DKPLog, EventRule 的 ViewSets
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class DKPLogViewSet(viewsets.ModelViewSet):
    queryset = DKPLog.objects.all()
    serializer_class = DKPLogSerializer

class EventRuleViewSet(viewsets.ModelViewSet):
    queryset = EventRule.objects.all()
    serializer_class = EventRuleSerializer

# 批量创建 Player 视图
@api_view(['POST'])
def bulk_create_players(request):
    if isinstance(request.data, list):  # 检查是否传入列表格式
        serializer = PlayerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Expected a list of players"}, status=status.HTTP_400_BAD_REQUEST)
