# Generated by Django 4.1.1 on 2022-10-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_alter_reserva_cantidadhabitaciones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='usuario',
        ),
        migrations.AddField(
            model_name='reserva',
            name='apellidos',
            field=models.CharField(blank=True, max_length=45, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='nombres',
            field=models.CharField(blank=True, max_length=45, verbose_name='Nombres'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='numeroDocumento',
            field=models.CharField(blank=True, max_length=45, verbose_name='Cédula de Ciudadanía'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, verbose_name='Teléfono'),
        ),
    ]
