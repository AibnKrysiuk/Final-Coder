from django import forms
from .models import Ship

class ShipFormulario(forms.ModelForm):
    
    class Meta:
        model = Ship
        fields = ['nombre', 'descripcion', 'price', 'imagen']