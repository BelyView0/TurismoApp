from django import forms
from .models import Lugar, Hotel

class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'descripcion', 'ubicacion', 'imagen']

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nombre', 'descripcion', 'direccion', 'precio', 'telefono', 'sitio_web', 'imagen']