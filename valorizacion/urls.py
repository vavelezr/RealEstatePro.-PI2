from django.urls import path
from . import views

urlpatterns = [ 
    path('calculo/', views.calculo, name='calculo'),
]