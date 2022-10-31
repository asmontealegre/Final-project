from django.shortcuts import render
from habitacion.models import Habitacion
# Create your views here.

def sedes(request):
    habitacion_s= Habitacion.objects.filter(sede="estacion",tipoHabitacion__nombreTipoHabitacion="Sencilla")[0]
    habitacion_d= Habitacion.objects.filter(sede="estacion",tipoHabitacion__nombreTipoHabitacion="Doble")[0]
    habitacion_c= Habitacion.objects.filter(sede="estacion",tipoHabitacion__nombreTipoHabitacion="Campestre")[0]
    habitaciones=[habitacion_s,habitacion_d,habitacion_c]

   

    context={
        'habitaciones': habitacion_s,
        'habitacion_d': habitacion_d,
        'habitacion_c': habitacion_c,
        'habitaciones': habitaciones
    }
    return render(request,'habitacion/sedes.html',context)

def habitaciones(request):
    context={ 
    }
    return render(request,'habitacion/habitaciones.html',context)