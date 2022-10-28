from django.shortcuts import render, redirect
from pqrs.forms import pqrsForms

from pqrs.models import PQRS


# Create your views here.

def pqrs(request):
    titulo="PQRS"
    pqrs=PQRS.objects.all()
    context={
        'titulo':titulo,
        'pqrs':pqrs
    }
    return render(request,'pqrs/pqrs.html',context)
    
    
def pqrs_registrada(request):
    titulo="PQRS Registradas"
    if request.method == "POST":
        form= pqrsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pqrs")
        else:
            print("Error")
    else:
        form=pqrsForms()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'pqrs/pqrs-registrada.html',context)
    
    
    