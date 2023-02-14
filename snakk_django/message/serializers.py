from rest_framework import serializers

from .models import Message

from userprofile.serializers import UserSerializer

class MessageSerializer(serializers):
    to_user = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = (
            'channel',
            'to_user',
            'content',
            'created_at',
            'created_by', 
        )