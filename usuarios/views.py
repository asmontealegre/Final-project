

from django.shortcuts import redirect, render
from django.contrib import messages
from usuarios.forms import UsuarioForms
from usuarios.models import Usuario

# Create your views here.


def usuarios(request):
    titulo="Ver Usuarios"
    usuarios=Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
    }
    return render(request,'usuarios/usuarios.html',context)
    
    
def usuarios_crear(request):
    titulo="Crear Usuarios"
    if request.method == "POST":
        form= UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se creo el Usuario ({request.POST['nombres']}) exitosamente!"
            )
            return redirect("usuarios")
        else:
            print("Error")
    else:
        form=UsuarioForms()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'usuarios/usuarios-crear.html',context)
    
def usuarios_editar(request, pk):
    titulo="Editar - Usuarios"
    usuario=Usuario.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioForms(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.info(
                request,f"Se modifico el Usuario ({request.POST['nombres']}) exitosamente!"
            )
            return redirect("usuarios")
        else:
            messages.error(
                request,f"Error al modificar el Usuario ({request.POST['nombres']})!"
            )
            print("Error al guardar")
    else:
        form=UsuarioForms(instance=usuario)
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'usuarios/usuarios-crear.html',context)  

def usuarios_eliminar(request, pk):
    titulo="Usuarios - Eliminar"
    usuarios= Usuario.objects.all()

    Usuario.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('usuarios')
        
   
    context={
        'usuarios':usuarios,
        'titulo':titulo,
     
    }
    return render(request,'usuarios/usuarios.html',context)
    
def login(request):
    titulo="Crear Usuarios"
    if request.method == "POST":
        form= UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios")
        else:
            print("Error")
    else:
        form=UsuarioForms()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'usuarios/usuarios-crear.html',context)