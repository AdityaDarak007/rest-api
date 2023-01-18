from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is Similar to a traditional Django view',
            'Gives you the most control over your appilcation logic'
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
