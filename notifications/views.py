from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification
from django.http import JsonResponse

@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(recipient=request.user, is_read=False)
    return render(request, 'notifications_list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, recipient=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications_list')


@login_required
def unread_notifications_count(request):
    count = Notification.objects.filter(recipient=request.user, is_read=False).count()
    return JsonResponse({"unread_count": count})