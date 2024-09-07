from django import forms


class PropertyForm(forms.Form):
    BARRIOS_CHOICES = [
        ("El Poblado", "El Poblado"),
        ("Laureles", "Laureles-Estadio"),
        ("Belén", "Belén"),
        ("La América", "La América"),
        ("Villa Hermosa", "Villa Hermosa"),
        ("Robledo", "Robledo"),
        ("Castilla", "Castilla"),
        ("Buenos Aires", "Buenos Aires"),
        ("San Antonio de Prado", "San Antonio de Prado"),
        ("Aranjuez", "Aranjuez"),
        ("Doce de Octubre", "Doce de Octubre"),
        ("San Javier", "San Javier"),
        ("Manrique", "Manrique"),
        ("Santa cruz", "Santa Cruz"),
        ("Barrio Popular", "Popular"),
    ]

    TIPO_CHOICES = [
        ("apartamento", "Apartamento"),
        ("casa", "Casa"),
    ]

    neighbourhood = forms.ChoiceField(choices=BARRIOS_CHOICES, label="Ingrese Barrio")
    direccion = forms.CharField(max_length=100, label="Dirección de la propiedad")
    type = forms.ChoiceField(choices=TIPO_CHOICES, label="Seleccionar")
    latitude = forms.CharField(max_length=50)
    longitude = forms.CharField(max_length=50)
    price = forms.IntegerField()
    num_rooms = forms.IntegerField()
    num_banos = forms.IntegerField()
    size = forms.FloatField(label="Tamaño (Área)")
    price_administration = forms.IntegerField()
    age = forms.IntegerField()
    garajes = forms.IntegerField()
    stratum = forms.IntegerField(min_value=1, max_value=6)
    id = forms.IntegerField()
