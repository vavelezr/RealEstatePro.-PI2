from django.urls import path
from . import views

urlpatterns = [
    path("calculate/", views.calculate, name="calculate"),
    path('property/edit/<int:property_id>/', views.edit_property, name='edit_property'),  
]