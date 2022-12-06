# Generated by Django 4.1.3 on 2022-12-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_usuario_tipodocumento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipoDocumento',
            field=models.CharField(choices=[('Cédula de Ciudadanía', 'Cédula de Ciudadanía'), ('Cédula de Extranjería', 'Cédula de Extranjería'), ('Pasaporte', 'Pasaporte'), ('Tarjeta de Identidad', 'Tarjeta de Identidad'), ('Otro Tipo de Documento', 'Otro Tipo de Documento')], default='Cédula de Ciudadanía', max_length=25, verbose_name='Tipo de Documento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.CharField(choices=[('Administración', 'Administrador'), ('Recepción', 'Recepción')], default='Recepción', max_length=20, verbose_name='Tipo Usuario'),
        ),
    ]
