# Generated by Django 5.1.6 on 2025-02-13 09:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_alter_friendrequest_unique_together_friendship'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='status',
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends_2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together={('user1', 'user2')},
        ),
    ]
