from django.urls import path

from reserva.views import crear_reserva, reserva

urlpatterns = [
    path('',reserva,name='reservar'),
    path('Reser/', crear_reserva,name="crear-reserva"),
    
    ]