from django.contrib import admin

from pqrs.models import PQRS, RespuestaPQRS

# Register your models here.
admin.site.register(PQRS)
admin.site.register(RespuestaPQRS)