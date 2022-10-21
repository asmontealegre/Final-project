from django.utils.translation import gettext_lazy as _
from django.db import models
from habitacion.models import TipoHabitacion
# Create your models here.

# Promocion.
class Promocion(models.Model):
    nombrePromocion=models.CharField(max_length=45, verbose_name="Nombre Promocion") 
    valor=models.CharField(max_length=6, verbose_name="Valor Habitacion")
    descripcionPromocion=models.CharField(max_length=80, verbose_name="Descripcion Promocion")
    fechaInicio=models.DateField(verbose_name="Fecha de Inicio", help_text=u"MM/DA/AAAA")
    fechaFin=models.DateField(verbose_name="Fecha de Final", help_text=u"MM/DA/AAAA")
    class Estado(models.TextChoices):
        ACTIVO='1', ('Activo')
        INACTIVO='0', ('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    TipoHabitacion=models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, verbose_name="Tipo Habitacion")
