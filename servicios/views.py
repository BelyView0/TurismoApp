from django.shortcuts import render, get_object_or_404, redirect
from .models import Lugar, Hotel, Restaurante
from .forms import LugarForm, HotelForm, RestauranteForm

def index_admin(request):
    return render(request, 'servicios/index_admin.html')
def index_usuario(request):
    return render(request, 'servicios/index_usuario.html')

# CRUD de Lugares
def lugar_list(request):
    lugares = Lugar.objects.all()
    return render(request, 'servicios/lugares/lugar_list.html', {'lugares': lugares})

def lugar_detail(request, pk):
    lugar = get_object_or_404(Lugar, pk=pk)
    return render(request, 'servicios/lugares/lugar_detail.html', {'lugar': lugar})

def lugar_create(request):
    if request.method == 'POST':
        form = LugarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lugar_list')
    else:
        form = LugarForm()
    return render(request, 'servicios/lugares/lugar_form.html', {'form': form})

def lugar_update(request, pk):
    lugar = get_object_or_404(Lugar, pk=pk)
    if request.method == 'POST':
        form = LugarForm(request.POST, request.FILES, instance=lugar)
        if form.is_valid():
            form.save()
            return redirect('lugar_list')
    else:
        form = LugarForm(instance=lugar)
    return render(request, 'servicios/lugares/lugar_form.html', {'form': form})

def lugar_delete(request, pk):
    lugar = get_object_or_404(Lugar, pk=pk)
    if request.method == 'POST':
        lugar.delete()
        return redirect('lugar_list')
    return render(request, 'servicios/lugares/lugar_confirm_delete.html', {'lugar': lugar})

# CRUD de Hoteles
def hotel_list(request):
    hoteles = Hotel.objects.all()
    return render(request, 'servicios/hoteles/hotel_list.html', {'hoteles': hoteles})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'servicios/hoteles/hotel_detail.html', {'hotel': hotel})

def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form = HotelForm()
    return render(request, 'servicios/hoteles/hotel_form.html', {'form': form})

def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'servicios/hoteles/hotel_form.html', {'form': form})

def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotel_list')
    return render(request, 'servicios/hoteles/hotel_confirm_delete.html', {'hotel': hotel})

# CRUD de Restaurantes
def restaurante_list(request):
    restaurantes = Restaurante.objects.all()
    return render(request, 'servicios/restaurantes/restaurante_list.html', {'restaurantes': restaurantes})

def restaurante_detail(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    return render(request, 'servicios/restaurantes/restaurante_detail.html', {'restaurante': restaurante})

def restaurante_create(request):
    if request.method == 'POST':
        form = RestauranteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurante_list')
    else:
        form= RestauranteForm()
    return render(request, 'servicios/restaurantes/restaurante_form.html', {'form': form})

def restaurante_update(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        form = RestauranteForm(request.POST, request.FILES, instance=restaurante)
        if form.is_valid():
            form.save()
            return redirect('restaurante_list')
    else:
        form = RestauranteForm(instance=restaurante)
    return render(request, 'servicios/restaurantes/restaurante_form.html', {'form': form})

def restaurante_delete(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        restaurante.delete()
        return redirect('restaurante_list')
    return render(request, 'servicios/restaurantes/restaurante_confirm_delete.html', {'restaurante': restaurante})

