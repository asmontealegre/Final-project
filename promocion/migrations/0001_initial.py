# Generated by Django 4.1.1 on 2022-10-21 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habitacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePromocion', models.CharField(max_length=45, verbose_name='Nombre Promocion')),
                ('valor', models.CharField(max_length=6, verbose_name='Valor Habitacion')),
                ('descripcionPromocion', models.CharField(max_length=80, verbose_name='Descripcion Promocion')),
                ('fechaInicio', models.DateField(help_text='MM/DA/AAAA', verbose_name='Fecha de Inicio')),
                ('fechaFin', models.DateField(help_text='MM/DA/AAAA', verbose_name='Fecha de Final')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('TipoHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitacion.tipohabitacion', verbose_name='Tipo Habitacion')),
            ],
        ),
    ]
