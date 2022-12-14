# Generated by Django 4.1.3 on 2022-12-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_usuario_email_usuario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipoDocumento',
            field=models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extrangería'), ('P.P', 'Pasaporte'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro Tipo de Documento')], default='C.C', max_length=5, verbose_name='Tipo de Documento'),
        ),
    ]
