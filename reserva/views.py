
from django.shortcuts import redirect, render
from reserva.forms import ReservaForms
from reserva.models import Reserva

# Create your views here.
def reserva(request):
    titulo="Usuarios Registrados"
    reserva=Reserva.objects.all()
    context={
        'titulo':titulo,
        'reserva':reserva
        
    }
    return render(request,'reserva/usuario-registrado.html',context)

def crear_reserva(request):
    titulo="Crear Reserva"
    if request.method == "POST":
        form= ReservaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reserva")
        else:
            print("Error")
    else:
        form=ReservaForms()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'reserva/crear-reserva.html',context)