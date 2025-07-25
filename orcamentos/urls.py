from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndicadorViewSet

router = DefaultRouter()
router.register(r'indicadores', IndicadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
