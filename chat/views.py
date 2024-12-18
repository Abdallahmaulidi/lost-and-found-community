from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from items.models import Item
from .models import Conversation, Message
from django.http import JsonResponse
import json
from django.urls import reverse
from notifications.utils import send_notification

@login_required
def get_unread_count(request):
    count = Message.objects.filter(
        conversation__participants=request.user,
        read=False
    ).exclude(sender=request.user).count()
    return JsonResponse({'count': count})

@login_required
def start_conversation(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        initial_message = data.get('message')
        
        # Check if conversation already exists
        conversation = Conversation.objects.filter(
            participants=request.user,
            item=item
        ).first()
        
        if not conversation:
            conversation = Conversation.objects.create(item=item)
            conversation.participants.add(request.user, item.posted_by)
            
            # Create the initial message
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=initial_message
            )
            
            # Send notification to item founder
            send_notification(
                item.posted_by,
                f"New message about your item: {item.title}",
                item
            )
        
        return JsonResponse({
            'success': True,
            'chat_url': reverse('chat:conversation_detail', args=[conversation.id])
        })
    
    return JsonResponse({'success': False}, status=400)

@login_required
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(
        Conversation.objects.prefetch_related('messages'),
        id=conversation_id,
        participants=request.user
    )
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=content
            )
    
    return render(request, 'chat/conversation.html', {
        'conversation': conversation
    })

@login_required
def conversations_list(request):
    conversations = Conversation.objects.filter(
        participants=request.user
    ).prefetch_related('messages')
    
    return render(request, 'chat/conversations_list.html', {
        'conversations': conversations
    })