from django import forms


class PropertyForm(forms.Form):
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
    direccion = forms.CharField(max_length=100, label="Dirección de la propiedad")
    type = forms.ChoiceField(choices=TIPO_CHOICES, label="Seleccionar")
    #latitude = forms.CharField(max_length=50)
    #longitude = forms.CharField(max_length=50)
    #price = forms.IntegerField()
    num_rooms = forms.IntegerField(min_value=0)
    num_banos = forms.IntegerField(min_value=0)
    size = forms.FloatField(label="Tamaño (Área)")
    price_administration = forms.IntegerField(min_value=0)
    age = forms.IntegerField(min_value=0)
    garajes = forms.IntegerField(min_value=0)
    stratum = forms.IntegerField(min_value=1, max_value=6)
    # id = forms.IntegerField()
