from django.shortcuts import render



# Create your views here.


def login(request):
    context={   
    }
    return render(request,'registration/login.html',context)



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