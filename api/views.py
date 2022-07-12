from api.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





class ProductList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):

        return Response(           
            {
            },
            status=status.HTTP_200_OK,
        )
