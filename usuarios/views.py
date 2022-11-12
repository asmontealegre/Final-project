from django.shortcuts import redirect, render
from django.contrib import messages
from usuarios.forms import UsuarioForms
from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password



# Create your views here.

@login_required(login_url='inicio')
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
        form= UsuarioForms(request.POST, request.FILES)
        if form.is_valid():
            if  not User.objects.filter(username=request.POST['numeroDocumento']):
                user = User.objects.create_user('nombres','email@email','pass')
                user.username= request.POST['numeroDocumento']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['email']
                user.password=make_password("@" + request.POST['nombres'][0] + request.POST['apellidos'][0]+"." + request.POST['numeroDocumento'][-4:])
                user.save()
            else:
                user=User.objects.get(username=request.POST['numeroDocumento'])

            usuario= Usuario.objects.create(
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                email=request.POST['email'],
                tipoDocumento=request.POST['tipoDocumento'],
                numeroDocumento=request.POST['numeroDocumento'],
                telefono=request.POST['telefono'],  
                tipoUsuario=request.POST['tipoUsuario'],
                user=user,
            )
            return redirect('usuarios')
        else:
            form = UsuarioForms(request.POST,request.FILES)
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

