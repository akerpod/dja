from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BotMessageViewSet, dashboard

router = DefaultRouter()
router.register('messages', BotMessageViewSet)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('', include(router.urls)),
]
