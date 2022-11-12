from django.views.defaults import page_not_found
from django.shortcuts import render


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
