from django.shortcuts import render, get_object_or_404, redirect
from .arima import *
from .models import RentalProperty
from .forms import PropertyForm

def rent(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            neighbourhood = form.cleaned_data["neighbourhood"]
            type = form.cleaned_data["type"]
            num_rooms = form.cleaned_data["num_rooms"]
            num_banos = form.cleaned_data["num_banos"]
            size = form.cleaned_data["size"]
            age = form.cleaned_data["age"]
            wifi = 1 if form.cleaned_data["wifi"] else 0
            air_conditioner = 1 if form.cleaned_data["air_conditioner"] else 0
            balcony = 1 if form.cleaned_data["balcony"] else 0
            terrace = 1 if form.cleaned_data["terrace"] else 0
            garden = 1 if form.cleaned_data["garden"] else 0
            pool = 1 if form.cleaned_data["pool"] else 0
            heater = 1 if form.cleaned_data["heater"] else 0
            washing_machine = 1 if form.cleaned_data["washing_machine"] else 0
            dryer = 1 if form.cleaned_data["dryer"] else 0
            chimney = 1 if form.cleaned_data["chimney"] else 0
            jacuzzi = 1 if form.cleaned_data["jacuzzi"] else 0
            sauna = 1 if form.cleaned_data["sauna"] else 0
            board_games = 1 if form.cleaned_data["board_games"] else 0
            parking = 1 if form.cleaned_data["parking"] else 0

            data_property = {
                "Ubicación": neighbourhood,
                "tipo_propiedad": type,
                "Habitaciones": num_rooms,
                "Baños": num_banos,
                "tamaño(m2)": size,
                "Wi-Fi": wifi,
                "aire_acondicionado": air_conditioner,
                "Balcón": balcony,
                "Terraza": terrace,
                "Jardín": garden,
                "Piscina": pool,
                "age": age,
                "Calefacción": heater,
                "Lavadora": washing_machine,
                "Secadora": dryer,
                "Chimenea": chimney,
                "Jacuzzi": jacuzzi,
                "Sauna": sauna,
                "juegos_de_mesa": board_games,
                "Parqueadero": parking,
            }

            data = get_csv_data()
            predictions = arimax_prediction(data_property, data)
            formatted_predictions = f'{predictions:,.2f}'
            data_property["price_per_night"] = formatted_predictions

            if 'save_property' in request.POST:
                RentalProperty.objects.create(
                    user=request.user,
                    neighbourhood=neighbourhood,
                    type=type,
                    num_rooms=num_rooms,
                    num_banos=num_banos,
                    size=size,
                    age=age,
                    wifi=wifi,
                    air_conditioner=air_conditioner,
                    balcony=balcony,
                    terrace=terrace,
                    garden=garden,
                    pool=pool,
                    heater=heater,
                    washing_machine=washing_machine,
                    dryer=dryer,
                    chimney=chimney,
                    jacuzzi=jacuzzi,
                    sauna=sauna,
                    board_games=board_games,
                    parking=parking,
                    price_per_night=predictions
                    )
                return redirect('profile')

            print("Formulario validado")
            print(data_property)
            return render(
                request, "rent.html", {"form": form, "results": data_property}
            )

    else:
        form = PropertyForm()

    return render(request, "rent.html", {"form": form})

def edit_rental_property(request, property_id):
    rental_property_instance = get_object_or_404(RentalProperty, id=property_id, user=request.user)

    if request.method == "POST":
        form = PropertyForm(request.POST, instance=rental_property_instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PropertyForm(instance=rental_property_instance)

    return render(request, 'rent.html', {'form': form, 'property': rental_property_instance})
