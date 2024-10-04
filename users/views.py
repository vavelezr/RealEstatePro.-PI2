
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomLoginForm, UserRegisterForm
from django.shortcuts import render
from valorizacion.models import Property

def profile_view(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, "profile.html", {"properties": properties})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Registro exitoso')
            return redirect("login")
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "register.html", context)


class CustomLoginView(LoginView):
    form_class = CustomLoginForm


def custom_logout(request):
    logout(request)
    return redirect("/")
