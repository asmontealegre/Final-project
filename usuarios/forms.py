

from django import forms

from usuarios.models import Usuario

class UsuarioForms(forms.ModelForm):
    class Meta:
        model=Usuario
        exclude=['user','estado']
        fields='__all__'