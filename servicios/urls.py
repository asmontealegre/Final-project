
from django.urls import path

from servicios.views import servicios


urlpatterns = [
    path('',servicios,name='servicios'),
]