from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """Test Api View"""

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