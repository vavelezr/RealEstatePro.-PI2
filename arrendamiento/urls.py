from django.urls import path
from . import views

urlpatterns = [
    path("rent/", views.rent, name="rent"),
    path('editar-arrendamiento/<int:property_id>/', views.edit_rental_property, name='edit_rental_property'),
]