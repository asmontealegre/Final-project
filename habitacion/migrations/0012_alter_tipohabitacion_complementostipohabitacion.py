# Generated by Django 4.1.1 on 2022-10-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitacion', '0011_alter_tipohabitacion_complementostipohabitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipohabitacion',
            name='complementosTipoHabitacion',
            field=models.CharField(max_length=200, verbose_name='Complementos Tipo Habitacion'),
        ),
    ]
