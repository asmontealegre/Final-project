from django.urls import path

from reserva.views import crear_reserva, reserva,abrir_reserva_usuario, reserva_eliminar

urlpatterns = [
    path('',reserva,name='reservar'),
    path('Reser/', crear_reserva,name="crear-reserva"),
    path('Reservar/',abrir_reserva_usuario,name="reservar-formulario"),
    path('Reservar/<int:pk>/',abrir_reserva_usuario,name="reservar-formulario"),
    path('user-eliminar/<int:pk>',reserva_eliminar,name="reserva-eliminar"),
    ]