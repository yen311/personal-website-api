from django.db import models

# Create your models here.

class Education(models.Model):
    name = models.CharField(
        max_length=50, 
        default=None, 
        blank=True, 
    ) 
    city = models.CharField(
        max_length=50, 
        default=None, 
        blank=True, 
    ) 
    country = models.CharField(
        max_length=50, 
        default=None, 
        blank=True, 
    )
    major = models.CharField(
        max_length=50, 
        default=None, 
        blank=True, 
    ) 
    description = models.TextField(
        max_length=50, 
        default=None, 
        blank=True, 
    ) 
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"{self.name}"