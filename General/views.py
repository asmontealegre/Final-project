from urllib import request
from django.shortcuts import render


def inicio(request):
    context={
        
    }
    return render(request,"index.html",context)

def inicioAdmin(request):
    titulo="Tablero Principal"
    context={
        'titulo':titulo
    }
    return render(request,'index-admin.html', context)