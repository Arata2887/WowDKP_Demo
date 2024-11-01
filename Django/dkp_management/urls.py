
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, DKPLogViewSet, EventRuleViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'dkp_logs', DKPLogViewSet)
router.register(r'event_rules', EventRuleViewSet)  # 注册 EventRule 的路由

urlpatterns = [
    path('', include(router.urls)),
]
