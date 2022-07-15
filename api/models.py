from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Education(models.Model):
    name = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    ) 
    city = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    ) 
    country = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    )
    major = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    ) 
    descriptions = ArrayField(models.CharField(max_length=255), blank=True, null=True, default=None)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"{self.name}"

class WorkExperience(models.Model):
    company = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    ) 
    city = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    ) 
    country = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    )
    position = models.CharField(
        max_length=255, 
        default=None, 
        blank=True, 
    ) 
    descriptions = ArrayField(models.CharField(max_length=255), blank=True, null=True, default=None)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"{self.position} at {self.company} "