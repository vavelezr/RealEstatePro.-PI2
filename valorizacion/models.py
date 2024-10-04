from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relates the property to the user
    neighbourhood = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    num_rooms = models.IntegerField()
    num_banos = models.IntegerField()
    size = models.DecimalField(max_digits=10, decimal_places=2)
    price_administration = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    age = models.IntegerField()
    garajes = models.IntegerField()
    stratum = models.IntegerField()
    estimated_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    #nightly_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.type} in {self.neighbourhood}"