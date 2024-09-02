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
    num_habitaciones = forms.IntegerField(label="Número de habitaciones")
    num_banos = forms.IntegerField(label="Número de baños")
    tamano = forms.IntegerField(label="Tamaño propiedad en m2")
    
    
    #los booleanos
    wifi = forms.BooleanField(label="Wi-Fi", required=False)
    aire_acondicionado = forms.BooleanField(label="Aire acondicionado", required=False)
    balcon = forms.BooleanField(label="Balcón", required=False)
    terraza = forms.BooleanField(label="Terraza", required=False)
    jardin = forms.BooleanField(label="Jardín", required=False)
    piscina = forms.BooleanField(label="Piscina", required=False)
    calefaccion = forms.BooleanField(label="Calefacción", required=False)
    lavadora = forms.BooleanField(label="Lavadora", required=False)
    secadora = forms.BooleanField(label="Secadora", required=False)
    chimenea = forms.BooleanField(label="Chimenea", required=False)
    jacuzzi = forms.BooleanField(label="Jacuzzi", required=False)
    sauna = forms.BooleanField(label="Sauna", required=False)
    juegos_de_mesa = forms.BooleanField(label="Juegos de mesa", required=False)
    parqueadero = forms.BooleanField(label="Parqueadero", required=False)
