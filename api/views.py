import json
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

class SkillList(APIView):
    def post(self, request):
    
        data = json.loads(request.body)
        type = data['type']
      
        if type == "Software":
            s = Skill.objects.filter(type="Software").order_by("type")
        elif type == "Data":
            s = Skill.objects.filter(type="Data").order_by("type")
        elif type == "Tool":
            s = Skill.objects.filter(type="Tool").order_by("type")
        elif type == "SoftSkill":
            s = Skill.objects.filter(type="SoftSkill").order_by("type")
        else:
            s = Skill.objects.all().order_by("type")

        s = s.order_by("percentage")
        skills = serializers.SkillSerializer(s, many=True);

        return Response(           
            {
                "skills":  skills.data,
            },
            status=status.HTTP_200_OK,
        )


class CourseList(APIView):
    def get(self, request):
        c = Course.objects.all().order_by("code")
        courses = serializers.CourseSerializer(c, many=True);
        
        return Response(           
            {
                "courses":  courses.data,
            },
            status=status.HTTP_200_OK,
        )
