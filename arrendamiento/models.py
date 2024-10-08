from django.db import models
from django.contrib.auth.models import User

class RentalProperty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    num_rooms = models.IntegerField()
    num_banos = models.IntegerField()
    size = models.FloatField()
    age = models.IntegerField()
    wifi = models.BooleanField(default=False)
    air_conditioner = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    heater = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    dryer = models.BooleanField(default=False)
    chimney = models.BooleanField(default=False)
    jacuzzi = models.BooleanField(default=False)
    sauna = models.BooleanField(default=False)
    board_games = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.neighbourhood} - {self.type} - {self.price_per_night}"
