from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from posts.models import Like, Comment
from chat.models import ChatMessage
from friends.models import FriendRequest

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created and instance.user != instance.post.user:
        Notification.objects.create(
            recipient=instance.post.user,
            sender=instance.user,
            notification_type='like',
            post=instance.post
        )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created and instance.user != instance.post.user:
        Notification.objects.create(
            recipient=instance.post.user,
            sender=instance.user,
            notification_type='comment',
            comment=instance
        )

@receiver(post_save, sender=ChatMessage)
def create_message_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.receiver,
            sender=instance.sender,
            notification_type='message',
            message=instance
        )

@receiver(post_save, sender=FriendRequest)
def create_friend_request_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            recipient=instance.receiver,
            sender=instance.sender,
            notification_type='friend_request'
        )

