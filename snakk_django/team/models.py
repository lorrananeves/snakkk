import uuid

from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)
    created_by = models.ForeignKey(User, related_name='owned_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
