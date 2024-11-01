from django.contrib import admin
from .models import Player, DKPLog, EquipmentType, Raid, Boss, EventRule

# 注册模型到管理后台
admin.site.register(Player)
admin.site.register(DKPLog)
admin.site.register(EquipmentType)
admin.site.register(Raid)
admin.site.register(Boss)
admin.site.register(EventRule)