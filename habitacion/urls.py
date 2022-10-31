from django.urls import path

from habitacion.views import  habitaciones, sedes 

urlpatterns = [
    path('',sedes,name='sedes'),
    path('habitaciones/', habitaciones,name="habitaciones"),
]
