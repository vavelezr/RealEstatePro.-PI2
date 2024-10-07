from django import forms

class PropertyForm(forms.ModelForm):

    BARRIOS_CHOICES = [
        ("Calasanz", "Calasanz"),
        ("Laureles", "Laureles"),
        ("El Poblado", "El Poblado"),
        ("Robledo", "Robledo"),
        ("Las Lomitas", "Las Lomitas"),
        ("Las Palmas", "Las Palmas"),
        ("Zuñiga", "Zuñiga"),
        ("Loma del Indio", "Loma del Indio"),
        ("Loma de las brujas", "Loma de las brujas"),
        ("La candelaria", "La candelaria"),
        ("Pan de azucar", "Pan de azucar"),
        ("Suramerica", "Suramerica"),
        ("Buenos Aires", "Buenos Aires"),
        ("Boston", "Boston"),
        ("Escobero", "Escobero"),
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
    wifi = forms.BooleanField(required=False, label="Wi-Fi")
    air_conditioner = forms.BooleanField(required=False, label="Aire acondicionado")
    balcony = forms.BooleanField(required=False, label="Balcón")
    terrace = forms.BooleanField(required=False, label="Terraza")
    garden = forms.BooleanField(required=False, label="Jardín")
    pool = forms.BooleanField(required=False, label="Piscina")
    heater = forms.BooleanField(required=False, label="Calefacción")
    washing_machine = forms.BooleanField(required=False, label="Lavadora")
    dryer = forms.BooleanField(required=False, label="Secadora")
    chimney = forms.BooleanField(required=False, label="Chimenea")
    jacuzzi = forms.BooleanField(required=False, label="Jacuzzi")
    sauna = forms.BooleanField(required=False, label="Sauna")
    board_games = forms.BooleanField(required=False, label="Juegos de mesa")
    parking = forms.BooleanField(required=False, label="Parqueadero")
