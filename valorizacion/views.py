from django.shortcuts import render
from .forms import PropertyForm
from .arima_test import *


def calculo(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        print(form.errors)
        if form.is_valid():
            barrio = form.cleaned_data["barrio"]
            latitud = form.cleaned_data["latitud"]
            longitud = form.cleaned_data["longitud"]
            tipo = form.cleaned_data["tipo"]
            precio = form.cleaned_data["precio"]
            num_habitaciones = form.cleaned_data["num_habitaciones"]
            num_banos = form.cleaned_data["num_banos"]
            tamano = form.cleaned_data["tamano"]
            precio_administracion = form.cleaned_data["precio_administracion"]
            antiguedad = form.cleaned_data["antiguedad"]
            garajes = form.cleaned_data["garajes"]
            estrato = form.cleaned_data["estrato"]
            propiedad_id = form.cleaned_data["id"]

            datos_propiedad = {
                "neighbourhood": barrio,
                "latitude": latitud,
                "longitude": longitud,
                "property_type": tipo,
                "price": precio,
                "rooms": num_habitaciones,
                "baths": num_banos,
                "area": tamano,
                "administration_price": precio_administracion,
                "age": antiguedad,
                "garages": garajes,
                "stratum": estrato,
                "id": propiedad_id,
                "valor_estimado": precio,
            }

            data = GetCsvData()
            predictions = ArimaxPrediction(datos_propiedad, data)

            datos_propiedad["valor_estimado"] = predictions  # f'{predictions[0]:.5f}'

            print("Forms validado")
            print(datos_propiedad)
            # Retornar los datos procesados al template
            return render(
                request, "calculo.html", {"form": form, "resultado": datos_propiedad}
            )

    else:
        form = PropertyForm()

    return render(request, "calculo.html", {"form": form})
