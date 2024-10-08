from django import forms
from .models import RentalProperty

class PropertyForm(forms.ModelForm):
    class Meta:
        model = RentalProperty
        fields = [
            'neighbourhood', 'num_rooms', 'num_banos', 'size', 'age',
            'wifi', 'air_conditioner', 'balcony', 'terrace', 'garden',
            'pool', 'heater', 'washing_machine', 'dryer', 'chimney', 
            'jacuzzi', 'sauna', 'board_games', 'parking'
        ]
        
    BARRIOS_CHOICES = [
        ("laureles","Laureles"),
        ("el poblado","El Poblado"),
        ("belén","Belén"),
        ("castilla","Castilla"),
        ("popular","Popular"),
        ("villa hermosa","Villa Hermosa"),
        ("Aranjuez", "aranjuez"),
        ("manrique","Manrique"),
        ("doce de octubre","Doce de Octubre"),
        ("santa cruz","Santa Cruz"),
        ("robledo","Robledo"),
        ("buenos aires","Buenos Aires"),
        ("la américa","La América"),
        ("san antonio de prado","San Antonio de Prado"),
    ]

    TIPO_CHOICES = [
        ("apartamento", "Apartamento"),
        ("casa", "Casa"),
    ]

    neighbourhood = forms.ChoiceField(choices=BARRIOS_CHOICES, label="Ingrese Barrio")
    type = forms.ChoiceField(choices=TIPO_CHOICES, label="Seleccionar")
    num_rooms = forms.IntegerField(min_value=0)
    num_banos = forms.IntegerField(min_value=0)
    size = forms.FloatField(label="Tamaño (Área)")
    age = forms.IntegerField(min_value=0)
    wifi = forms.BooleanField(required=False)#, label="Wi-Fi")
    air_conditioner = forms.BooleanField(required=False)#, label="Aire acondicionado")
    balcony = forms.BooleanField(required=False)#, label="Balcón")
    terrace = forms.BooleanField(required=False)#, label="Terraza")
    garden = forms.BooleanField(required=False)#, label="Jardín")
    pool = forms.BooleanField(required=False)#, label="Piscina")
    heater = forms.BooleanField(required=False)#, label="Calefacción")
    washing_machine = forms.BooleanField(required=False)#, label="Lavadora")
    dryer = forms.BooleanField(required=False)#, label="Secadora")
    chimney = forms.BooleanField(required=False)#, label="Chimenea")
    jacuzzi = forms.BooleanField(required=False)#, label="Jacuzzi")
    sauna = forms.BooleanField(required=False)#, label="Sauna")
    board_games = forms.BooleanField(required=False)#, label="Juegos de mesa")
    parking = forms.BooleanField(required=False)#, label="Parqueadero")
