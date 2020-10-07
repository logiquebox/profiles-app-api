from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings 

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
  def put(self, request, pk=None):
    """Handles updating an object"""
    return Response({'method': 'PUT'})

  
  def patch(self, request, pk=None):
    """Partially updates an object"""
    return Response({'method': 'PATCH'})

  
  def delete(self, request, pk=None):
    """Handles deleting an object"""
    return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
  """Test Api viewset"""

  serializer_class = serializers.HelloSerializer

  def list(self, request):
    """Returns a Hello message"""

    a_viewset = [
      'Uses actions (list, create, update, partial_update, retrieve)',
      'Automatically routes to URLS using routers',
      'provides more functionality with less code'
    ]

    context = {
      'message':'Hello',
      'a_viewset': a_viewset
    }

    return Response(context)


  
  def create(self, request):
    """Returns a hello message with the user's name"""

    serializer_class = serializers.HelloSerializer
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello {name}' 
      return Response({'message': message})
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  def retrieve(self, request, pk=None):
    """Handles getting an object by its ID"""
    return Response({'http_method': 'GET'})
  

  def update(self, request, pk=None):
    """Handles updating an object"""
    return Response({'http_method':'PUT'})

  
  def partial_update(self, request, pk=None):
    """Handles updating part of an object"""
    return Response({'http_method':'PATCH'})
  

  def destroy(self, request, pk=None):
    """Handles removing or deleting an object"""
    return Response({'http_method':'DELETE'})
    


class UserProfileViewSet(viewsets.ModelViewSet):
  """Handle creating and updating user profile"""

  serializer_class = serializers.UserProfileSerializer
  queryset = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'email',)


  
class UserLoginApiView(ObtainAuthToken):
  """Handles creating authentication tokens"""
  renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




    
  