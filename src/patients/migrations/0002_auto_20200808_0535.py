# Generated by Django 3.0.6 on 2020-08-08 05:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('nutritionists', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='patient', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
                ('weight', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)], verbose_name='peso')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='cumpleaños')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='edad')),
                ('height', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(1)], verbose_name='estatura')),
                ('body_mass', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='masa corporal')),
                ('body_fat', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='grasa corporal')),
                ('body_muscle', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='músculo corporal')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Síntoma',
                'verbose_name_plural': 'Síntomas',
            },
        ),
        migrations.AddField(
            model_name='medicaltracing',
            name='nutritionist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracings', to='nutritionists.Nutritionist', verbose_name='nutriolgo'),
        ),
        migrations.AddField(
            model_name='medicaltracing',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracings', to='patients.Patient', verbose_name='paciente'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='diseases',
            field=models.ManyToManyField(related_name='records', to='patients.Disease', verbose_name='enfermedades'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='nutritionist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='nutritionists.Nutritionist', verbose_name='nutriolgo'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='patients.Patient', verbose_name='paciente'),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='symptoms',
            field=models.ManyToManyField(related_name='records', to='patients.Symptom', verbose_name='síntomas'),
        ),
    ]