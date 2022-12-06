from django.shortcuts import render, redirect
from reserva.forms import ReservaForms, ReservaDetalleForms
from reserva.models import Reserva, DetalleReserva
from habitacion.models import Habitacion

# Create your views here.


def reservas_formulario(request):
    context = {
    }
    return render(request, 'reserva/reservar-formulario.html', context)


def reserva(request):
    titulo = "Usuarios Resgistrados"
    reserva = Reserva.objects.all()
    context = {
        'titulo': titulo,
        'reserva': reserva
    }
    return render(request, 'reserva/usuario-registrado.html', context)


def crear_reserva(request):
    titulo = "Crear Reservas"
    if request.method == "POST":
        form = ReservaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reserva")
        else:
            print("Error")
    else:
        form = ReservaForms()
    context = {
        'titulo': titulo,
        'form': form
    }
    return render(request, 'reserva/crear-reserva.html', context)


def abrir_reserva_usuario(request, pk=None):
    titulo = "Crear Reservas"
    form = None
    reservas = DetalleReserva.objects.filter(reserva_id=pk)
    if pk:
        reserva = Reserva.objects.get(id=pk)
    else:
        reserva = None
    if request.method == "POST" and 'abrir-reserva' in request.POST:

        form = ReservaForms(request.POST)

        if form.is_valid():

            aux = form.save()
            return redirect("reservar-formulario", pk=aux.id)
        else:
            print("Error")
    if request.method == "POST" and 'agregar-habitacion' in request.POST:
        for habitacion in range(int(request.POST['cantidad'])):
            hab = Habitacion.objects.filter(
                tipoHabitacion__nombreTipoHabitacion= request.POST['habitacion'],disponibilidad='Disponible')
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", hab)

            if hab:
                aux = DetalleReserva.objects.create(
                habitacion=hab[0],
                reserva_id=pk
            )
            else:
                print("No hay habitaciones disponibles")
            
        return redirect("reservar-formulario", pk=pk)

    context = {
        'titulo': titulo,
        'form': form,
        'reserva': reserva,
        'reservas': reservas
    }
    return render(request, 'reserva/reservar-formulario.html', context)


def reserva_eliminar(request, pk):
    titulo="Reserva - Eliminar"
    reserva= Reserva.objects.all()

    Reserva.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('reservar')
        
   
    context={
        'reserva':reserva,
        'titulo':titulo,
     
    }
    return render(request,'reserva/usuario-registrado.html',context)
    

        