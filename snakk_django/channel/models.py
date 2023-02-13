import uuid

from django.db import models

from team.models import Team

class Channel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    team = models.ForeignKey(Team, related_name='channels', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)