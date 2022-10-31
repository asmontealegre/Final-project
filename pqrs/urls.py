from django.urls import path

from pqrs.views import pqrs, pqrs_eliminar, pqrs_registrada

urlpatterns = [
    path('',pqrs,name='pqrs'),
    path('pqrs/',pqrs_registrada,name="pqrs-registrada"),
    path('pqrs-eliminar/<int:pk>',pqrs_eliminar,name="pqrs-eliminar"),
]