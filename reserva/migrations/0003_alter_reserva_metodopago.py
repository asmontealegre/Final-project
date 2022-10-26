# Generated by Django 4.1.1 on 2022-10-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_alter_reserva_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='metodoPago',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia Bancaria', 'Transferencia Bancaria')], default='Efectivo', max_length=30, verbose_name='Método de Pago'),
        ),
    ]