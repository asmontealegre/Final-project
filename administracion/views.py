from django.shortcuts import render
from reserva.models import Reserva
from usuarios.models import Usuario
from pqrs.models import PQRS

def administracion(request):
    titulo="Tablero Principal"
    cantidad_reserva= Reserva.objects.all().count()
    cantidad_usuarios= Usuario.objects.all().count()
    cantidad_pqrs= PQRS.objects.all().count()

    labels_stock=[]
    data_stock=[]
    reserva= Reserva.objects.all().order_by('nombres')
    for reserva in reserva:
        labels_stock.append(reserva.nombres)
        data_stock.append(reserva.apellidos)

    context={
        'titulo': titulo,
        'cantidad_usuarios':cantidad_usuarios,
        'cantidad_reserva':cantidad_reserva,
        'cantidad_pqrs':cantidad_pqrs,
        'labels_stock':labels_stock,
        'data_stock':data_stock,
    }
    return render(request,'administracion/index-admin.html',context)



def login(request):
    context={   
    }
    return render(request,'registration/login.html',context)

def usuarios(request):
    titulo="Usuarios"
    context={
        'titulo':titulo
    }
    return render(request,'usuarios/usuarios.html',context)


def error_404(request,exception):
    return page_not_found(request,'404.html')


def loggedIn(request):
    if request.user.is_authenticated:
        respuesta:"Ingresado como "+ request.user.username
    else:
        respuesta:"No estas autenticado."
    return HttpResponse(respuesta)

def logout(request):    

    return redirect("registration/login.html")