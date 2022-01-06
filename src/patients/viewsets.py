"""Patients Viewsets."""
from .models import (
    Patient,
    Disease,
    Symptom,
    MedicalRecord,
)
from .serializers import (
    PatientSerializer,
    DiseaseSerializer,
    SymptomSerializer,
    MedicalRecordSerializer,
)
from rest_framework.viewsets import ModelViewSet


class PatientViewSet(ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DiseaseViewSet(ModelViewSet):

    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class SymptomViewSet(ModelViewSet):

    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


class MedicalRecordViewSet(ModelViewSet):

    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
