from django.urls import path

from . import views

urlpatterns = [
     path("resume/", views.ResumeList.as_view()),
     path("skill/", views.SkillList.as_view()),
     path("course/", views.CourseList.as_view()),
     
]