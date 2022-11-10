
from django import forms

from reserva.models import Reserva,DetalleReserva



class ReservaForms(forms.ModelForm):
    class Meta:
        model=Reserva
        exclude= ['valorReserva','metodoPago','estado']

class ReservaDetalleForms(forms.ModelForm):
    class Meta:
        model=DetalleReserva
        exclude=['reserva']
