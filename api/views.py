from api import serializers
from api.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class ResumeList(APIView):

    def get(self, request):
        e = Education.objects.all().order_by("-startDate")
        educations = serializers.EducationSerializer(e, many=True);

        w = WorkExperience.objects.all().order_by("-startDate")
        workExperience = serializers.WorkExperienceSerializer(w, many=True);

        p = Project.objects.all().order_by("-date")
        projects = serializers.ProjectSerializer(p, many=True);
        
        return Response(           
            {
                "educations":  educations.data,
                "workExperience": workExperience.data,
                "projects": projects.data,
            },
            status=status.HTTP_200_OK,
        )

