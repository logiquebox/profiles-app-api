from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
  """Test Api View"""
  serializer_class = serializers.HelloSerializer


  def get(self, request, format=None):
    """Returns a list of APIView features"""
    an_apiview = [
      'Uses HTTP methods as functions (get, post, push, patch, delete)',
      'Similar to the traditional Django view',
      'Gives you full comtrol over your application logic',
      'Is mapped manually to URLs',
    ]

    context = {
      'message': 'Hello!',
      'an_apiview': an_apiview
    }

    return Response(context)
  
  def post(self, request):
    """creates a hello message with our name"""
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name} '

      return Response({'message': message}) 
    else:
      return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)