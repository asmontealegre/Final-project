from django.shortcuts import render
from habitacion.models import Habitacion
# Create your views here.


def sedes(request):
    context={ 
    }
    return render(request,'habitacion/sedes.html',context)

def habitaciones(request):
    context={ 
    }
    return render(request,'habitacion/habitaciones.html',context)