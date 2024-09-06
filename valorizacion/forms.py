from django import forms

class PropertyForm(forms.Form):
    BARRIOS_CHOICES = [
        ('el_poblado', 'El Poblado'),
        ('laureles_estadio', 'Laureles-Estadio'),
        ('belen', 'Belén'),
        ('la_america', 'La América'),
        ('villa_hermosa', 'Villa Hermosa'),
        ('robledo', 'Robledo'),
        ('castilla', 'Castilla'),
        ('buenos_aires', 'Buenos Aires'),
        ('san_antonio_de_prado', 'San Antonio de Prado'),
        ('aranjuez', 'Aranjuez'),
        ('doce_de_octubre', 'Doce de Octubre'),
        ('san_javier', 'San Javier'),
        ('manrique', 'Manrique'),
        ('santa_cruz', 'Santa Cruz'),
        ('popular', 'Popular'),
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

