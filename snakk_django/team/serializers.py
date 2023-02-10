from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Team

from userprofile.serializers import UserSerializer

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'members',
            'created_by'
        )