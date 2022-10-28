
from django.urls import path

from administracion.views import   login, administracion
from usuarios.views import usuarios

urlpatterns = [
    path('',login,name="login"),
    path('adm/', administracion,name='index-admin'),
    path('',usuarios,name="usuarios"),
    
    
    
    
    
]