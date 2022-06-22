from api.models import *
from api.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class ProductList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(           
            {
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
