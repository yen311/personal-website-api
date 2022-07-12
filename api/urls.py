from django.urls import path

from . import views

urlpatterns = [
     path("resume/", views.ProductList.as_view()),
]