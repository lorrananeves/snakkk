from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Channel
from .serializers import ChannelSerializer
from team.models import Team

@api_view(['POST'])
def new_channel(request):
    team_id = request.data.get('team_id')
    name = request.data.get('name')
    team = Team.objects.filter(members_is=[request.user.id]).get(pk=team_id)
    channel = Channel.objects.create(name=name, team=team)
    serializer = ChannelSerializer(channel)

    return Response(serializer.data)
