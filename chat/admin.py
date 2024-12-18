from django.contrib import admin
from .models import Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('item__title', 'participants__username')
    date_hierarchy = 'created_at'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'conversation', 'created_at', 'read')
    list_filter = ('read', 'created_at')
    search_fields = ('content', 'sender__username')
    date_hierarchy = 'created_at'