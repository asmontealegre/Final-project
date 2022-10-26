from django.db import models
from django.core.validators import MinValueValidator
from habitacion.models import Habitacion
from promocion.models import Promocion
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario

# Create your models here.

# Reserva.
class Reserva(models.Model):
    cantidadHabitaciones=models.IntegerField(validators=[MinValueValidator(0)], verbose_name=" Cantidad de Habitaciones")
    numeroHuespedes=models.IntegerField(validators=[MinValueValidator(0)], verbose_name=" Número de Huespedes")
    
    valorReserva=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Valor Reserva")
    
    class metodoPago(models.TextChoices):
        Efectivo='Efectivo', _('Efectivo')
        TransferenciaBancaria='Transferencia Bancaria', _('Transferencia Bancaria')
    metodoPago=models.CharField(max_length=30, choices=metodoPago.choices, default=metodoPago.Efectivo, verbose_name="Método de Pago")
    
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    

# Detalle Reserva.
class DetalleReserva(models.Model):
    fechaIngreso=models.DateField(verbose_name="Fecha de Ingres", help_text=u"MM/DA/AAAA")
    fechaSalida=models.DateField(verbose_name="Fecha de Salida", help_text=u"MM/DA/AAAA")
    Habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitacion")
    Reserva=models.ForeignKey(Reserva, on_delete=models.CASCADE, verbose_name="Reserva")
    Promocion=models.ForeignKey(Promocion, on_delete=models.CASCADE, verbose_name="Promocion")