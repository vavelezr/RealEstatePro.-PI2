from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    usable_password = None
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''  
    )
    password2 = forms.CharField(
        label='Confirma contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=''  
    )
    username = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': '', 
            'password1': '', 
            'password2': '',  
        }


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control' })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control' })
    )
    