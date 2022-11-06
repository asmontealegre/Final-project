from django.urls import path

from habitacion.views import  habitaciones, reservas_d_b, reservas_d_e, reservas_e_b, reservas_e_e, reservas_s_b, reservas_s_e, sedes 

urlpatterns = [
    path('',sedes,name='sedes'),
    path('habitaciones/', habitaciones,name="habitaciones"),
    path('Reservar_sencilla_la_estacion/',reservas_s_e,name="reservas_s_e"),
    path('Reservar_doble_la_estacion/',reservas_d_e,name="reservas_d_e"),
    path('Reservar_especial_la_estacion/',reservas_e_e,name="reservas_e_e"),
    path('Reservar_sencilla_el_bosque/',reservas_s_b,name="reservas_s_b"),
    path('Reservar_doble_el_bosque/',reservas_d_b,name="reservas_d_b"),
    path('Reservar_especial_el_bosque/',reservas_e_b,name="reservas_e_b"),
]

