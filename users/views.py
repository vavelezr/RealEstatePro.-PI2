from functools import reduce

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomLoginForm, UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            # messages.success(request, f"Usuario {username} creado")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "register.html", context)


class CustomLoginView(LoginView):
    form_class = CustomLoginForm

def custom_logout(request):
    logout(request)
    return redirect('/')
