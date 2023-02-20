from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import MessageSerializer

from team.models import Team

@api_view(['GET'])
def get_messages(request, team_id):
    team = Team.objects.filter(members_in=[request.user.id]).get(pk=team_id)
    serializer = MessageSerializer(team.messages.all())
    return Response(serializer.data)

