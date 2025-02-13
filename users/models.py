from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    bio = models.TextField(blank=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.username
