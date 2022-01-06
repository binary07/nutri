"""Appointments Viewsets."""
from .models import (
    Appointment,
    Contact,
)

from .serializers import (
    AppointmentSerializer,
    ContactSerializer,
)

from rest_framework.viewsets import ModelViewSet    


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(patient=self.request.user)
        return query_set


class AppointmentViewSet(ModelViewSet):

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(patient=self.request.user)
        return query_set
