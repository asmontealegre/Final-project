"""General URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from General.views import  error_404 

from General.views import loggedIn,logout
from django.contrib.auth.views import LoginView as login

handler404= error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",login.as_view(),name="inicio"),
    path('promocion/', include('promocion.urls')),
    path('servicios/',include('servicios.urls')),
    path('adm/',include('administracion.urls')),
    path('user/',include('usuarios.urls')),
    path('reser/',include('reserva.urls')),
    path('habit/',include('habitacion.urls')),
    path('pqrs/',include('pqrs.urls')),

    path('loggedin/',loggedIn,name="inicio-sesion"),
    path('logout/',logout,name="fin-sesion"),
    


    
]