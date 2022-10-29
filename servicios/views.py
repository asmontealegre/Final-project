from django.shortcuts import render

# Create your views here.
def servicios(request):
    context={ 
    }
    return render(request,'servicios/servicios.html',context)