
from django.urls import path
from administracion.views import administracion, usuarios_crear

urlpatterns = [
    path('', administracion,name='administracion'),
    path('Crear/', usuarios_crear,name='usuarios-crear'),
    
]