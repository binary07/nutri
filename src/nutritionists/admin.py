"""Nutritionists App Admin."""
from django.contrib import admin
from .models import (
    Nutritionist,
    Specialty
)

# Register your models here.
admin.site.register(Nutritionist)
admin.site.register(Specialty)
