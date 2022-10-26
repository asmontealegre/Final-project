
from django.contrib import admin

from usuarios.models import Tipo_Usuario, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tipo_Usuario)