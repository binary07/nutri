# Generated by Django 3.0.6 on 2020-08-08 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Cita', 'verbose_name_plural': 'Citas'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
    ]
