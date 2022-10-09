from django.urls import path

from promocion.views import promocion

urlpatterns = [
    path('',promocion,name='promocion'),
]

