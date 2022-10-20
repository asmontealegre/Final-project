from django.db import models

# Create your models here.

# Tipo Habitacion.
class TipoHabitacion(models.Model):
    class NombreTipoHabitacion(models.Model):
        Sencilla='Sencilla', ('Sencilla')
        Doble='Doble', ('Doble')
        Campestre='Campestre', ('Campestre')
    nombreTipoHabitacion=models.CharField(max_length=10, choices=NombreTipoHabitacion.choices, default=NombreTipoHabitacion.Sencilla, verbose_name="Nombre Tipo de Habitacion")
    valorTipoHabitacion=models.CharField(_max_length=6, verbose_name="Valor Tipo Habitacion")
    descripcionTipoHabitacion=models.CharField(_max_length=200, verbose_name="Descripcion Tipo Habitacion")
    capacidad=models.CharField(_max_length=45, verbose_name="Capacidad")
    class Estado(models.Model):
        ACTIVO='1', ('Activo')
        INACTIVO='0', ('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, Verbose_name="Estado")


# Habitacion.
class Habitacion(models.Model):
    numeroHabitacion=models.CharField(_max_length=3, verbose_name="Numero de Habitacion")
    class Estado(models.Model):
        ACTIVO='1', ('Activo')
        INACTIVO='0', ('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, Verbose_name="Estado")
    class Disponibilidad(models.Model):
        DISPONIBLE='Disponible', ('Disponible')
        OCUPADA='Ocupada', ('Ocupada')
    disponibilidad=models.CharField(max_length=1, choices=Disponibilidad.choices, default=Disponibilidad.DISPONIBLE, Verbose_name="Disponibilidad")
    TipoHabitacion=models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE, verbose_name="Tipo Habitacion")