from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'message', 'item', 'read', 'created_at')
    list_filter = ('read', 'created_at')
    search_fields = ('message', 'recipient__username', 'item__title')
    date_hierarchy = 'created_at'