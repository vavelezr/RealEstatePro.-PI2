from django.urls import path
from . import views

urlpatterns = [
    path('venta', views.mapa_view, name='mapa'),
    path('alquiler', views.mapa_alquiler_view, name='mapa'),
]
