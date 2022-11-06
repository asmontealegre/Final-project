from django.shortcuts import render
from habitacion.models import Habitacion
# Create your views here.

def reservas_s_e(request):
    context={ 
    }
    return render(request,'habitacion/reserva_s_e.html',context)

def reservas_d_e(request):
    context={ 
    }
    return render(request,'habitacion/reserva_d_e.html',context)

def reservas_e_e(request):
    context={ 
    }
    return render(request,'habitacion/reserva_e_e.html',context)

def reservas_s_b(request):
    context={ 
    }
    return render(request,'habitacion/reserva_s_b.html',context)

def reservas_d_b(request):
    context={ 
    }
    return render(request,'habitacion/reserva_d_b.html',context)

def reservas_e_b(request):
    context={ 
    }
    return render(request,'habitacion/reserva_e_b.html',context)

def sedes(request):
    context={ 
    }
    return render(request,'habitacion/sedes.html',context)

def habitaciones(request):
    context={ 
    }
    return render(request,'habitacion/habitaciones.html',context)