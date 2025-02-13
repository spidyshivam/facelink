from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class FriendRequest(models.Model):
    sender = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('sender', 'receiver')

class Friendship(models.Model):
    user1 = models.ForeignKey(CustomUser, related_name='friends_1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(CustomUser, related_name='friends_2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user1', 'user2')
