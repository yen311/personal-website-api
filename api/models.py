from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

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
    descriptions = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        null=True,
        default=None,
    )
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
    descriptions = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        null=True,
        default=None,
    )
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return f"{self.position} at {self.company}"


class Project(models.Model):
    name = models.CharField(
        max_length=255,
        default=None,
        blank=True,
    )
    dropdownName = models.CharField(
        max_length=255,
        default=None,
        blank=True,
    )
    descriptions = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        null=True,
        default=None,
    )
    techStacks = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        null=True,
        default=None,
    )
    date = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    githubUrl = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    path = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    url = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    img = models.ImageField(
        upload_to="uploads/",
        default=None,
        blank=True,
        null=True,
    )
    detail = models.TextField(
        default=None,
        blank=True,
        null=True,
    )
    TYPE_CHOICES = (
        ("Personal", "Personal"),
        ("Uni", "Uni"),
        ("Work", "Work"),
    )
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default="Personal",
    )

    def __str__(self):
        return f"{self.name}"


class Skill(models.Model):
    TYPE_CHOICES = (
        ("Software", "Software"),
        ("Data", "Data"),
        ("Tool", "Tool"),
        ("SoftSkill", "SoftSkill"),
    )

    name = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        default="Software",
    )
    percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    code = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    url = models.CharField(
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"
