from django.contrib.auth.models import User
from django.db import models

from channel.models import Channel
from team.models import Team

class Message(models.Model):
    GROUP = 'group'
    DM = 'dm'

    CHOICES_MESSAGE_TYPE = (
        (GROUP, 'group'),
        (DM, 'Direct message')
    )

    team = models.ForeignKey(Team, related_name='messages', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, blank=True, null=True)
    channel = models.ForeignKey(Channel, related_name='messages', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    message_type = models.CharField(max_length=20, choices=CHOICES_MESSAGE_TYPE, default=GROUP)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.ForeignKey(User, related_name='sant_messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)