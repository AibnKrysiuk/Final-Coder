from django import forms
from .models import Ship

class ShipFormulario(forms.ModelForm):
    
    class Meta:
        model = Ship
        fields = ('__all__')