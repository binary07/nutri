"""User Model."""
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # TODO: Define fields here

    GENDER_CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )

    MEXICO_STATES = (
        ('Aguascalientes', 'Aguascalientes'),
        ('Baja California', 'Baja California'),
        ('Baja California Sur', 'Baja California Sur'),
        ('Campeche', 'Campeche'),
        ('Coahuila', 'Coahuila'),
        ('Colima', 'Colima'),
        ('Chiapas', 'Chiapas'),
        ('Chihuahua', 'Chihuahua'),
        ('CDMX', 'CDMX'),
        ('Durango', 'Durango'),
        ('Edo. Méx', 'Edo. Méx'),
        ('Guanajuato', 'Guanajuato'),
        ('Guerrero', 'Guerrero'),
        ('Hidalgo', 'Hidalgo'),
        ('Jalisco', 'Jalisco'),
        ('Michoacán', 'Michoacán'),
        ('Morelos', 'Morelos'),
        ('Nayarit', 'Nayarit'),
        ('Nuevo León', 'Nuevo León'),
        ('Oaxaca', 'Oaxaca'),
        ('Puebla', 'Puebla'),
        ('Queretaro', 'Queretaro'),
        ('Quintana Roo', 'Quintana Roo'),
        ('San Luis Potosí', 'San Luis Potosí'),
        ('Sinaloa', 'Sinaloa'),
        ('Sonora', 'Sonora'),
        ('Tabasco', 'Tabasco'),
        ('Tamaulipas', 'Tamaulipas'),
        ('Tlaxcala', 'Tlaxcala'),
        ('Veracruz', 'Veracruz'),
        ('Yucatán', 'Yucatán'),
        ('Zacatecas', 'Zacatecas'),
    )

    is_patient = models.BooleanField(
        'es paciente',
        default=False,
    )
    is_nutritionist = models.BooleanField(
        'es nutriologo',
        default=False,
    )
    second_lastname = models.CharField(
        'apellido materno',
        max_length=50,
        blank=True,
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="El número teléfonico debe ser: '+999999999'. Hasta 15 digitos."
    )
    phone = models.CharField(
        'teléfono',
        validators=[phone_regex],
        max_length=17,
        blank=True,
    )
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )
    residence_state = models.CharField(
        max_length=50,
        choices=MEXICO_STATES,
        blank=True,
        null=True,
    )


    class Meta:
        verbose_name = "Usario"
        verbose_name_plural = "Usarios"

    def __str__(self):
        return f'{self.username}'
