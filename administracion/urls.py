
from django.urls import path
from administracion.views import administracion

urlpatterns = [
    path('', administracion,name='administracion'),
]