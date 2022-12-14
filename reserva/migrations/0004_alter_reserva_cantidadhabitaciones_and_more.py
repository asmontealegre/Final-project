# Generated by Django 4.1.1 on 2022-10-26 07:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0003_alter_reserva_metodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantidadHabitaciones',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name=' Cantidad de Habitaciones'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='numeroHuespedes',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name=' Número de Huespedes'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='valorReserva',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Reserva'),
        ),
    ]
