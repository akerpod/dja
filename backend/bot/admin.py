from django.contrib import admin
from .models import BotMessage

@admin.register(BotMessage)
class BotMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'from_user', 'created_at')
    search_fields = ('user__username', 'text')
