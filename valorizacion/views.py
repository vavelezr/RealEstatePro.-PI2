from django.shortcuts import render, get_object_or_404, redirect
from .arima_test import *
from .forms import PropertyForm
from .models import Property



def calculate(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        print(form.errors)
        if form.is_valid():
            neighbourhood = form.cleaned_data["neighbourhood"]
            direccion = form.cleaned_data["direccion"]
            # latitude = form.cleaned_data["latitude"]
            # longitude = form.cleaned_data["longitude"]
            type = form.cleaned_data["type"]
            # price = form.cleaned_data["price"]
            num_rooms = form.cleaned_data["num_rooms"]
            num_banos = form.cleaned_data["num_banos"]
            size = form.cleaned_data["size"]
            price_administration = form.cleaned_data["price_administration"]
            age = form.cleaned_data["age"]
            garajes = form.cleaned_data["garajes"]
            stratum = form.cleaned_data["stratum"]
            # propiedad_id = form.cleaned_data["id"]

            data_property = {
                "neighbourhood": neighbourhood,
                "direccion": direccion,
                
                # "latitude": latitude,
                # "longitude": longitude,
                "property_type": type,
                # "price": price,
                "rooms": num_rooms,
                "baths": num_banos,
                "area": size,
                "administration_price": price_administration,
                "age": age,
                "garages": garajes,
                "stratum": stratum,
                "id": 1,
                # "price_estimated": price,
            }

            data = get_csv_data()
            predictions = arimax_prediction(data_property, data)

            formatted_predictions = {6 - i: f'{prediction:,.2f}' for i, prediction in enumerate(reversed(predictions))}
            data_property["price_estimated"] = formatted_predictions


            if 'save_property' in request.POST:
                Property.objects.create(
                    user=request.user,
                    neighbourhood=neighbourhood,
                    direccion=direccion,
                    type=type,
                    num_rooms=num_rooms,
                    num_banos=num_banos,
                    size=size,
                    price_administration=price_administration,
                    age=age,
                    garages=garajes,
                    stratum=stratum,
                    estimated_price=predictions[-1]
                )
                return redirect('profile')

            print("Forms validado")
            print(data_property)
            return render(
                request, "calculate.html", {"form": form, "results": data_property}
            )

    else:
        form = PropertyForm()

    return render(request, "calculate.html", {"form": form})



def edit_property(request, property_id):

    property_instance = get_object_or_404(Property, id=property_id, user=request.user)
    
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property_instance)  
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PropertyForm(instance=property_instance)
    
    return render(request, 'calculate.html', {'form': form, 'property': property_instance})