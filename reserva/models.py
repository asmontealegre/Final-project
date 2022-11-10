from django.db import models
from django.core.validators import MinValueValidator
from habitacion.models import Habitacion
from promocion.models import Promocion
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Reserva.
class Reserva(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres", blank=True) 
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos", blank=True)
    numeroDocumento=models.CharField(max_length=45, verbose_name="Cédula de Ciudadanía", blank=True)
    telefono=models.CharField(max_length=15, verbose_name="Teléfono", blank=True)
    correo = models.EmailField(verbose_name='Correo electrónico', null=True, blank=True)
    fechaIngreso=models.DateField(verbose_name="Check-In", help_text=u"MM/DA/AAAA",null=True, blank=True)
    fechaSalida=models.DateField(verbose_name="Check-Out", help_text=u"MM/DA/AAAA",null=True,  blank=True)
    valorReserva=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Valor Reserva",null=True,  blank=True)
    class metodoPago(models.TextChoices):
        Efectivo='Efectivo', _('Efectivo')
        TransferenciaBancaria='Transferencia Bancaria', _('Transferencia Bancaria')
    metodoPago=models.CharField(max_length=30, choices=metodoPago.choices, default=metodoPago.Efectivo, verbose_name="Método de Pago")
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "Reserva %s"%(self.numeroDocumento) 
    

# Detalle Reserva.
class DetalleReserva(models.Model):
    habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitacion")
    reserva=models.ForeignKey(Reserva, on_delete=models.CASCADE, verbose_name="Reserva")
    
    def __str__(self):
        return "DetalleReserva %s"%(self.reserva)
    
