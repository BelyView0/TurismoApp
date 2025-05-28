from django import forms
from .models import Lugar, Hotel, Restaurante

class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'descripcion', 'ubicacion', 'imagen']

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nombre', 'descripcion', 'direccion', 'precio', 'telefono', 'sitio_web', 'imagen']

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'descripcion', 'direccion', 'telefono', 'horario', 'imagen']
