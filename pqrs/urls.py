from django.urls import path

from pqrs.views import pqrs, pqrs_registrada 

urlpatterns = [
    path('',pqrs,name='pqrs'),
    path('pqrss/',pqrs_registrada,name="pqrs-registrada")
]