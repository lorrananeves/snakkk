from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Userprofile

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = (
            'id',
            'is_online',
        )

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserprofileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'userprofile',
            'get_full_name',
        )