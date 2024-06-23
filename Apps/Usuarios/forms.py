from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nombre de usuario',
            'class': 'input-class'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'class': 'input-class'
        })

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo electrónico',
            'class': 'input-class'
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nombre de usuario',
            'class': 'input-class'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'class': 'input-class'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirmar contraseña',
            'class': 'input-class'
        })

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']