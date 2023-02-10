from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer

@api_view(['GET'])
def get_my_information(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
