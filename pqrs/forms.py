from django import forms
from pqrs.models import PQRS


class PQRSForms(forms.ModelForm):
    class Meta:
        model=PQRS
        exclude=["estado"]
        
        
