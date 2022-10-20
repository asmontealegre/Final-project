from django.shortcuts import render

# Create your views here.

def habitacion(request):
    context={
        
    }
    return render(request,'habitacion/habitacion.html',context)