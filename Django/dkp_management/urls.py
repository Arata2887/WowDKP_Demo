from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, DKPLogViewSet, EventRuleViewSet, bulk_create_players

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'dkp_logs', DKPLogViewSet)
router.register(r'event_rules', EventRuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('players/bulk_create/', bulk_create_players),  # 批量创建 Player 的路由
]
