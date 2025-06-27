from rest_framework import serializers
from .models import BotMessage

class BotMessageSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BotMessage
        fields = ['id', 'user', 'user_username', 'text', 'from_user', 'created_at']
