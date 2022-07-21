from django.contrib import admin
from api.models import *

# Register your models here.

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass