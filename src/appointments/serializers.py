from .models import (
    Contact,
    Appointment,
)
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = [
            'id',
            'patient',
            'nutritionist'
        ]

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient',
            'nutritionist',
            'appointment_date'
        ]
