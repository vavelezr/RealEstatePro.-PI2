from django import forms

class PropertyForm(forms.Form):
    BARRIOS_CHOICES = [
        ('El Poblado', 'El Poblado'),
        ('Laureles', 'Laureles-Estadio'),
        ('Belén', 'Belén'),
        ('La América', 'La América'),
        ('Villa Hermosa', 'Villa Hermosa'),
        ('Robledo', 'Robledo'),
        ('Castilla', 'Castilla'),
        ('Buenos Aires', 'Buenos Aires'),
        ('San Antonio de Prado', 'San Antonio de Prado'),
        ('Aranjuez', 'Aranjuez'),
        ('Doce de Octubre', 'Doce de Octubre'),
        ('San Javier', 'San Javier'),
        ('Manrique', 'Manrique'),
        ('Santa cruz', 'Santa Cruz'),
        ('Barrio Popular', 'Popular'),
    ]

    TIPO_CHOICES = [
        ('apartamento', 'Apartamento'),
        ('casa', 'Casa'),
    ]

    
    barrio = forms.ChoiceField(choices=BARRIOS_CHOICES, label="Ingrese Barrio")
    direccion = forms.CharField(max_length=100, label="Dirección de la propiedad")
    tipo = forms.ChoiceField(choices=TIPO_CHOICES, label="Seleccionar")
    latitud = forms.CharField(max_length=50)
    longitud = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    num_habitaciones = forms.IntegerField()
    num_banos = forms.IntegerField()
    tamano = forms.FloatField(label='Tamaño (Área)')
    precio_administracion = forms.IntegerField()
    antiguedad = forms.IntegerField()
    garajes = forms.IntegerField()
    estrato = forms.IntegerField(min_value=1, max_value=6)
    id=forms.IntegerField()

