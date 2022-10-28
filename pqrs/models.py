
from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.
# PQRS.
class PQRS(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres",blank=True) 
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos",blank=True)
    telefono=models.CharField(max_length=15, verbose_name="Teléfono",blank=True)
    email=models.CharField(max_length=50, verbose_name="Correo Electronico", blank=True)
    asunto=models.CharField(max_length=45, verbose_name="Asunto")
    comentarioCliente=models.CharField(max_length=250, verbose_name="Comentario")
    fechaCreacion=models.DateField(verbose_name="Fecha", help_text=u"MM/DA/AAAA")
    
    
    

# Respuesta PQRS.
class RespuestaPQRS(models.Model):
    fechaRespuesta=models.DateField(verbose_name="Fecha de Respuesta", help_text=u"MM/DA/AAAA")
    respuestaPQRS=models.CharField(max_length=200, verbose_name="Respuesta PQRS")
    quienRespondePQRS=models.CharField(max_length=45, verbose_name="Quien Responde PQRS")
    canalRespuesta=models.CharField(max_length=45, verbose_name="Canal de Respuesta")
    class Estado(models.TextChoices):
        ACTIVO='1', ('Activo')
        INACTIVO='0', ('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    PQRS=models.ForeignKey(PQRS, on_delete=models.CASCADE, verbose_name="PQRS")


