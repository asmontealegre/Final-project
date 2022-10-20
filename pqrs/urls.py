from django.urls import path

from pqrs.views import pqrs 

urlpatterns = [
    path('',pqrs,name='pqrs'),
]