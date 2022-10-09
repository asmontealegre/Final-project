from urllib import request
from django.shortcuts import render


def holamundo(request):
    titulo="Inicio"
    nombre="Angelica Montealegre"

    context={
        "nombres" :nombre,
        "titulo" :titulo
    }
    return render(request,"index.html",context)