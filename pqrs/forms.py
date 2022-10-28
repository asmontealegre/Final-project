
from dataclasses import fields
from django import forms
from pqrs.models import PQRS



class pqrsForms(forms.ModelForm):
    class Meta:
        model=PQRS
        fields='__all__'