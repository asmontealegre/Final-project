from django.shortcuts import render



# Create your views here.
def login(request):
    context={   
    }
    return render(request,'administracion/login.html',context)


def administracion(request):
    titulo="Tablero Principal"
    context={
        'titulo': titulo
    }
    return render(request,'administracion/index-admin.html',context)


def usuarios(request):
    titulo="Usuarios"
    context={
        'titulo':titulo
    }
    return render(request,'usuarios/usuarios.html',context)


