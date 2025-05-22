from django.shortcuts import render, get_object_or_404, redirect
from .models import Lugar
from .forms import LugarForm

def index(request):
    return render(request, 'index.html')

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