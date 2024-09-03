from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomLoginForm, UserRegisterForm

# Create your views here.


def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else: 
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
