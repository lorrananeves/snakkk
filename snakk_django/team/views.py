from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Team
from .serializers import TeamSerializer

@api_view(['GET'])
def get_teams(request):
    teams = Team.objects.filter(members__in=[request.user.id])
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_team(request):
    data = request.data
    name = data.get('name')

    team = Team.objects.create(name=name, created_by=request.user)
    team.members.add(request.user)
    team.save()

    return Response({'message': 'created'})

@api_view(['GET'])
def get_team(request, team_id):
    team = Team.objects.filter(members_is=[request.user.id]).get(pk=team_id)
    serializer = TeamSerializer(team)
    return Response(serializer.data)