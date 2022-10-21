from django.db import models
from django.utils.translation import gettext_lazy as _
from administracion.models import Usuario
# Create your models here.
# PQRS.
class PQRS(models.Model):
    fechaCreacion=models.DateField(verbose_name="Fecha de Creacion", help_text=u"MM/DA/AAAA")
    asunto=models.CharField(max_length=45, verbose_name="Asunto")
    comentarioCliente=models.CharField(max_length=250, verbose_name="Comentario Cliente")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuarios")

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
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuarios")
    PQRS=models.ForeignKey(PQRS, on_delete=models.CASCADE, verbose_name="PQRS")


