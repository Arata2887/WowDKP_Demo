from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dkp_management.urls')),  # 导入 dkp_management 应用的所有路由
]
