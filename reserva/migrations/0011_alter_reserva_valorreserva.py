# Generated by Django 4.1.1 on 2022-11-09 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0010_rename_habitacion_detallereserva_habitacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='valorReserva',
            field=models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Valor Reserva'),
        ),
    ]
