from django import forms
from .models import Post

class PostFormulario(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'fecha', 'meGusta','imagen', 'texto']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }