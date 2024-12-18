from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Item
from notifications.utils import send_notification

@receiver(post_save, sender=Item)
def notify_matching_users(sender, instance, created, **kwargs):
    if created:
        # Get all users except the item poster
        users = User.objects.exclude(id=instance.posted_by.id)
        
        # Send notification to each user
        for user in users:
            send_notification(
                user,
                f"New {instance.get_status_display()} item posted: {instance.title}",
                instance
            )