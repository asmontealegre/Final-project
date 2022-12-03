
from django.urls import path
from usuarios.views import usuarios

from administracion.views import administracion, loggedIn,logout
from django.contrib.auth.views import LoginView as login


urlpatterns = [
    
    path("",login.as_view(),name="inicio"),
    path('',usuarios,name="usuarios"),
    path('adm/', administracion,name='index-admin'),
    path('loggedin/',loggedIn,name="inicio-sesion"),
    path('logout/',logout,name="fin-sesion"),
    
    
    
    
    
]