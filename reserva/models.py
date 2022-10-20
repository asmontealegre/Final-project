from django.db import models

# Create your models here.

# Reserva.
class Reserva(models.Model):
    cantidadHabitaciones=models.CharField(_max_length=2, verbose_name="Cantiadad de Habitaciones")
    numeroHuespedes=models.CharField(_max_length=2, verbose_name="Numero de Huespedes")
    valorReserva=models.CharField(_max_length=7, verbose_name="Valor de Reserva")
    metodoPago=models.CharField(_max_length=45, verbose_name="Metodo de Pago")
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, Verbose_name="Estado")
    Usuarios=models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name="Usuarios")

# Detalle Reserva.
class DetalleReserva(models.Model):
    fechaIngreso=models.DateField(verbose_name="Fecha de Ingres", help_text=u"MM/DA/AAAA")
    fechaSalida=models.DateField(verbose_name="Fecha de Salida", help_text=u"MM/DA/AAAA")
    Habitacion=models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Habitacion")
    Reserva=models.ForeignKey(Reserva, on_delete=models.CASCADE, verbose_name="Reserva")
    Promocion=models.ForeignKey(Promocion, on_delete=models.CASCADE, verbose_name="Promocion")