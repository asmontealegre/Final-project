from django.shortcuts import render
from administracion.forms import UsuarioForm

from administracion.models import Usuario

# Create your views here.

def administracion(request):
    context={
        
    }
    return render(request,'administracion/index-admin.html',context)

def usuarios_crear(request):
    titulo='Usuarios - Crear'
    form= UsuarioForm()
    context={
        'titulo' : titulo,
        'form':form
        
    }
    return render(request,'administracion/admin-crear.html',context)