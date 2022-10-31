# Generated by Django 4.1.1 on 2022-10-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuario_tipodocumento_usuario_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipoDocumento',
            field=models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extrangeriía'), ('P.P', 'Pasaporte'), ('T.I', 'Tarjeta de Identidad'), ('Otro', 'Otro Tipo de Documento')], default='C.C', max_length=5, verbose_name='Tipo de Documento'),
        ),
    ]
