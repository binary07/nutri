# Generated by Django 3.0.6 on 2020-09-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20200808_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaltracing',
            name='meal_type',
            field=models.CharField(blank=True, choices=[('Estandar', 'Estandar'), ('Perdida de Peso', 'Perdida de Peso'), ('Deportista', 'Deportista'), ('Vegano, Vegetariano', 'Vegano, Vegetariano'), ('Con Especificación', 'Con Especificación')], max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
