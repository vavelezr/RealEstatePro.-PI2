from django.shortcuts import render
from .forms import PropertyForm

def calculo(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # Obtener los datos del formulario
            barrio = form.cleaned_data['barrio']
            latitud = form.cleaned_data['latitud']
            longitud = form.cleaned_data['longitud']
            tipo = form.cleaned_data['tipo']
            precio = form.cleaned_data['precio']
            num_habitaciones = form.cleaned_data['num_habitaciones']
            num_banos = form.cleaned_data['num_banos']
            tamano = form.cleaned_data['tamano']
            precio_administracion = form.cleaned_data['precio_administracion']
            antiguedad = form.cleaned_data['antiguedad']
            garajes = form.cleaned_data['garajes']
            estrato = form.cleaned_data['estrato']
            propiedad_id = form.cleaned_data['id']

            datos_propiedad = {
                'barrio': barrio,
                'latitud': latitud,
                'longitud': longitud,
                'tipo': tipo,
                'precio': precio,
                'num_habitaciones': num_habitaciones,
                'num_banos': num_banos,
                'tamano': tamano,
                'precio_administracion': precio_administracion,
                'antiguedad': antiguedad,
                'garajes': garajes,
                'estrato': estrato,
                'id': propiedad_id,
            }
            
            print("Forms validado")
            print(datos_propiedad)
            # Retornar los datos procesados al template
            return render(request, 'calculo.html', {'form': form, 'resultado': datos_propiedad})

    else:
        form = PropertyForm()

    return render(request, 'calculo.html', {'form': form})
