from django.contrib import admin
from api.models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name","price")
    list_display = (
        "name",
        "price",
    )