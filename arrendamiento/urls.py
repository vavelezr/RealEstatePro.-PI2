from django.urls import path
from . import views

urlpatterns = [
    path("rent/", views.rent, name="rent"),
]