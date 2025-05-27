from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Perfil


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            # Verificar si tiene perfil; si no, lo crea en caliente
            try:
                perfil = user.perfil
            except Perfil.DoesNotExist:
                perfil = Perfil.objects.create(user=user)

            login(request, user)

            return redirect('index_admin' if perfil.es_admin else 'index_usuario')
        else:
            messages.error(request, 'Credenciales incorrectas')

    return render(request, 'usuarios/login.html')


def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        clave_admin = request.POST.get('clave_admin', '').strip()

        # Solo se asigna como admin si se pone la clave correcta
        es_admin = clave_admin == 'adminadd123'

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe')
            return redirect('registro')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        Perfil.objects.create(user=user, es_admin=es_admin)

        messages.success(request, 'Usuario creado exitosamente. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'usuarios/registro.html')




@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def index_usuario(request):
    if request.user.perfil.es_admin:
        return redirect('index_admin')
    return render(request, 'servicios/index_usuario.html')


@login_required
def index_admin(request):
    if not request.user.perfil.es_admin:
        return redirect('index_usuario')
    return render(request, 'servicios/index_admin.html')