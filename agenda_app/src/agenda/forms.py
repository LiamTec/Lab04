# agenda/forms.py
from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'email', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
