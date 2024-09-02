from django.shortcuts import render
from .forms import PropertyForm

def calculo(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            barrio = form.cleaned_data['barrio']
            direccion = form.cleaned_data['direccion']
            tipo = form.cleaned_data['tipo']
            num_habitaciones = form.cleaned_data['num_habitaciones']
            num_banos = form.cleaned_data['num_banos']
            tamano = form.cleaned_data['tamano']

            # Procesar las selecciones múltiples (checkboxes)
            datos_propiedad = {
                'barrio': barrio,
                'direccion': direccion,
                'tipo': tipo,
                'num_habitaciones': num_habitaciones,
                'num_banos': num_banos,
                'tamano': tamano,
                'wifi': form.cleaned_data.get('wifi', False),
                'aire_acondicionado': form.cleaned_data.get('aire_acondicionado', False),
                'balcon': form.cleaned_data.get('balcon', False),
                'terraza': form.cleaned_data.get('terraza', False),
                'jardin': form.cleaned_data.get('jardin', False),
                'piscina': form.cleaned_data.get('piscina', False),
                'calefaccion': form.cleaned_data.get('calefaccion', False),
                'lavadora': form.cleaned_data.get('lavadora', False),
                'secadora': form.cleaned_data.get('secadora', False),
                'chimenea': form.cleaned_data.get('chimenea', False),
                'jacuzzi': form.cleaned_data.get('jacuzzi', False),
                'sauna': form.cleaned_data.get('sauna', False),
                'juegos_de_mesa': form.cleaned_data.get('juegos_de_mesa', False),
                'parqueadero': form.cleaned_data.get('parqueadero', False),
            }
            print(datos_propiedad)
            return render(request, 'calculo.html', {'form': form, 'resultado': datos_propiedad})

    else:
        form = PropertyForm()

    return render(request, 'calculo.html', {'form': form})
