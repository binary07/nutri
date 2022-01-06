"""Patient App Admin."""
from django.contrib import admin
from .models import (
    Patient,
    Disease,
    Symptom,
    MedicalRecord,
)

# Register your models here.
admin.site.register(Patient)
admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(MedicalRecord)
