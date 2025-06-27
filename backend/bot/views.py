from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import BotMessage
from .serializers import BotMessageSerializer

class BotMessageViewSet(viewsets.ModelViewSet):
    queryset = BotMessage.objects.all().order_by('-created_at')
    serializer_class = BotMessageSerializer
    permission_classes = [permissions.IsAuthenticated]


def dashboard(request):
    return render(request, 'index.html')
