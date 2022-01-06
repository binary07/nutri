from django.db import models


class Specialty(models.Model):

    name = models.CharField('nombre', max_length=150)

    class Meta:
        verbose_name = "Especilidad"
        verbose_name_plural = "Especilidades"

    def __str__(self):
        return self.name


class Nutritionist(models.Model):

    user = models.OneToOneField(
        'users.User',
        primary_key=True,
        verbose_name='usuario',
        related_name='nutritionist',
        on_delete=models.CASCADE,
    )
    license = models.CharField(
        'cedula',
        max_length=100,
    )
    degree = models.CharField(
        'titulo',
        max_length=100,
    )
    specialties = models.ManyToManyField(
        'Specialty',
        verbose_name='especialidades',
        related_name='nutritionists',
    )

    def __str__(self):
        user = self.user
        return f'{user.first_name} {user.last_name} {user.second_lastname}'
