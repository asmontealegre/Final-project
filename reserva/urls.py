from django.urls import path

from reserva.views import crear_reserva, reserva, reservas_formulario

urlpatterns = [
    path('',reserva,name='reservar'),
    path('Reser/', crear_reserva,name="crear-reserva"),
    path('Reservar/',reservas_formulario,name="reservar-formulario"),
    ]