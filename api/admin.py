from django.contrib import admin
from api.models import *

# Register your models here.

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass
