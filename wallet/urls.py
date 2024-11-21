from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarteiraViewSet, TransacaoViewSet

router = DefaultRouter()
router.register(r'carteiras', CarteiraViewSet)
router.register(r'transacao', TransacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
