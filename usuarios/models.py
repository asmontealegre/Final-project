
from django.db import models

# Create your models here.
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User 

# Create your models here.


# Tipo Usuario.
class Tipo_Usuario(models.Model):
    class UsuarioTipo(models.TextChoices):
        Administrador='Administrador', ('Administrador')
        Recepción='Recepción', ('Recepción')
    usuarioTipo=models.CharField(max_length=14, choices=UsuarioTipo.choices, default=UsuarioTipo.Recepción, verbose_name="Usuario Tipo")
    contraseña=models.CharField(max_length=20, verbose_name="Contraseña")
    class Estado(models.TextChoices):
        ACTIVO=1, _('Activo')
        INACTIVO=0, _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

# Usuario.
class Usuario(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres") 
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    email= models.EmailField(max_length=150, verbose_name='correo')

    class TipoDocumento(models.TextChoices):
        CC='Cédula de Ciudadanía', _('Cédula de Ciudadanía')
        CE='Cédula de Extranjería', _('Cédula de Extranjería')
        PP='Pasaporte', _('Pasaporte')
        TI='Tarjeta de Identidad', _('Tarjeta de Identidad')
        OT='Otro Tipo de Documento', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=25, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=45, unique=True, verbose_name="Número de Documento")
    telefono=models.CharField(max_length=15, verbose_name="Teléfono", blank=True)
    
    class tipoUsuario(models.TextChoices):
        Administrador='Administración', _('Administrador')
        Recepción='Recepción', _('Recepción')
    tipoUsuario=models.CharField(max_length=20, choices=tipoUsuario.choices, default=tipoUsuario.Recepción, verbose_name="Tipo Usuario")
    
    class Estado(models.TextChoices):
        ACTIVO=1, ('Activo')
        INACTIVO=0, ('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    user=models.ForeignKey(User, on_delete= models.CASCADE)
