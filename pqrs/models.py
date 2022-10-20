from django.db import models

# Create your models here.

# Respuesta PQRS.
class RespuestaPQRS(models.Model):
    fechaRespuesta=models.DateField(verbose_name="Fecha de Respuesta", help_text=u"MM/DA/AAAA")
    respuestaPQRS=models.CharField(_max_length=200, verbose_name="Respuesta PQRS")
    quienRespondePQRS=models.CharField(_max_length=45, verbose_name="Quien Responde PQRS")
    canalRespuesta=models.CharField(_max_length=45, verbose_name="Canal de Respuesta")
    class Estado(models.Model):
        ACTIVO='1', ('Activo')
        INACTIVO='0', ('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, Verbose_name="Estado")
    Usuarios=models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name="Usuarios")
    PQRS=models.ForeignKey(PQRS, on_delete=models.CASCADE, verbose_name="PQRS")

# PQRS.
class PQRS(models.Model):
    fechaCreacion=models.DateField(verbose_name="Fecha de Creacion", help_text=u"MM/DA/AAAA")
    asunto=models.CharField(_max_length=45, verbose_name="Asunto")
    comentarioCliente=models.CharField(_max_length=250, verbose_name="Comentario Cliente")
    Usuarios=models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name="Usuarios")

