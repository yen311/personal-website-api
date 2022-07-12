from api import serializers
from api.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ResumeList(APIView):

    def get(self, request, format=None):
        educations = Education.objects.all()
        s = serializers.EducationSerializer(educations, many=True);
        return Response(           
            {
                "educations":  s.data
            },
            status=status.HTTP_200_OK,
        )
