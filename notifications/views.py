from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Notification
from django.urls import reverse

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(recipient=request.user)
    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications
    })

@login_required
def mark_as_read(request, notification_id):
    notification = Notification.objects.get(
        id=notification_id,
        recipient=request.user
    )
    notification.read = True
    notification.save()
    return JsonResponse({'status': 'success'})

@login_required
def get_unread_count(request):
    count = Notification.objects.filter(
        recipient=request.user,
        read=False
    ).count()
    return JsonResponse({'count': count})

@login_required
def get_unread_notifications(request):
    notifications = Notification.objects.filter(
        recipient=request.user,
        read=False
    ).order_by('-created_at')[:5]
    
    data = [{
        'id': n.id,
        'message': n.message,
        'url': reverse('item-detail', args=[n.item.id]) if n.item else None,
        'created_at': n.created_at.isoformat()
    } for n in notifications]
    
    return JsonResponse({'notifications': data})

@login_required
def mark_all_read(request):
    if request.method == 'POST':
        Notification.objects.filter(recipient=request.user, read=False).update(read=True)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=405)