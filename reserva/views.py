from django.shortcuts import render

# Create your views here.

def reserva(request):
    context={
        
    }
    return render(request,'reserva/reserva.html',context)

def usuarios(request):
    titulo="Usuarios"
    context={
        'titulo':titulo
    }
    return render(request,'usuarios/usuarios.html',context)