from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('message', 'Message'),
        ('friend_request', 'Friend Request'),
    )

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications", null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications", null=True)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('posts.Comment', on_delete=models.CASCADE, null=True, blank=True)
    message = models.ForeignKey('chat.ChatMessage', on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
