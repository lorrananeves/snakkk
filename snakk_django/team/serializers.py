from django.contrib.auth import models
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Team

from channel.serializers import ChannelSerializer
from userprofile.serializers import UserSerializer

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    channels = ChannelSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'members',
            'channels',
            'created_by'
        )