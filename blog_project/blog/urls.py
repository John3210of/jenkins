from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet

router = DefaultRouter()
router.register(r'', BoardViewSet)  # 기본 엔드포인트를 blog/로 설정
urlpatterns = [
    path('', include(router.urls)),
]
