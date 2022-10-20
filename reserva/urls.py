from django.urls import path

from reserva.views import reserva 

urlpatterns = [
    path('',reserva,name='reserva'),
]
