from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from django.urls import reverse

def send_notification(user, message, item=None):
    # Create notification in database
    notification = Notification.objects.create(
        recipient=user,
        message=message,
        item=item
    )
    
    # Send real-time notification
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user.id}",
        {
            "type": "notification_message",
            "message": message,
            "url": reverse('item-detail', args=[item.id]) if item else None
        }
    )
    
    return notification