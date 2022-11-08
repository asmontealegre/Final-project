from tkinter.tix import Form
from django.shortcuts import render, redirect
from pqrs.forms import PQRSForms

from pqrs.models import PQRS


# Create your views here.

def pqrs(request):
    titulo="PQRS"
    form= PQRSForms()
    pqrs=PQRS.objects.all()
    context={
        'titulo':titulo,
        'pqrs':pqrs,
        'form':form
    }
    return render(request,'pqrs/pqrs.html',context)
 
def pqrs_registrada(request):
    titulo="PQRS Registradas"
    if request.method == "POST":
        form= PQRSForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pqrs-registrada")
        else:
            form=PQRSForms(request.POST)
    else:
        form=PQRSForms()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'pqrs/pqrs-registrada.html',context)

def pqrs_eliminar(request, pk):
    titulo="Pqrs - Eliminar"
    pqrs= PQRS.objects.all()

    PQRS.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('pqrs')
        
   
    context={
        'pqrs':pqrs,
        'titulo':titulo,
     
    }
    return render(request,'pqrs/pqrs.html',context)


   