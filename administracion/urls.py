
from django.urls import path

from administracion.views import   login,  administracion, registrar
from usuarios.views import usuarios

urlpatterns = [
    path('',login,name="login"),
    path('registrar/',registrar,name="registrar"),
    path('adm/', administracion,name='index-admin'),
    path('',usuarios,name="usuarios"),
    
    
    
    
    
]