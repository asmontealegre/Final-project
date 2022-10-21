from django.contrib import admin
from reserva.models import DetalleReserva, Reserva

# Register your models here.
admin.site.register(Reserva)
admin.site.register(DetalleReserva)