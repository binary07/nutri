from django.db import models
from patients.models import Patient
from nutritionists.models import Nutritionist


class Contact(models.Model):
    patient = models.ForeignKey(
        Patient,
        verbose_name='paciente',
        on_delete=models.CASCADE,
    )

    nutritionist = models.ForeignKey(
        'nutritionists.Nutritionist',
        verbose_name='nutriolgo',
        on_delete=models.CASCADE,
    )

    has_been_contacted = models.BooleanField(
        default=True
    )

    contacted_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"


class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        verbose_name='paciente',
        on_delete=models.CASCADE,
    )

    nutritionist = models.ForeignKey(
        'nutritionists.Nutritionist',
        verbose_name='nutriolgo',
        on_delete=models.CASCADE,
    )

    appointment_date = models.DateTimeField(
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
