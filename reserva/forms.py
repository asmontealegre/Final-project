from dataclasses import fields
from django import forms

from reserva.models import Reserva



class ReservaForms(forms.ModelForm):
    class Meta:
        model=Reserva
        fields='__all__'