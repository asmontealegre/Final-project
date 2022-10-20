from django.urls import path

from habitacion.views import habitacion 

urlpatterns = [
    path('',habitacion,name='habitacion'),
]
