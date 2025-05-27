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

import re  # Asegúrate de tenerlo al inicio del archivo

def es_contrasena_segura(password):
    """Verifica que la contraseña cumpla con los requisitos mínimos de seguridad."""
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):  # al menos una mayúscula
        return False
    if not re.search(r'[a-z]', password):  # al menos una minúscula
        return False
    if not re.search(r'[0-9]', password):  # al menos un número
        return False
    if not re.search(r'[^A-Za-z0-9]', password):  # al menos un carácter especial
        return False
    return True

def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        clave_admin = request.POST.get('clave_admin', '').strip()

        # Validación de contraseña segura
        if not es_contrasena_segura(password):
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula, un número y un carácter especial.')
            return redirect('registro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('registro')

        es_admin = clave_admin == 'adminadd123'

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        Perfil.objects.create(user=user, es_admin=es_admin)

        messages.success(request, 'Usuario creado exitosamente. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'usuarios/registro.html')

import random
import string
from django.contrib.auth.models import User

def generar_contrasena_temporal(longitud=10):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def recuperar_contrasena(request):
    nueva_contrasena = None

    if request.method == 'POST':
        username = request.POST['username']

        try:
            user = User.objects.get(username=username)
            nueva_contrasena = generar_contrasena_temporal()
            user.set_password(nueva_contrasena)
            user.save()

            messages.success(request, 'Se ha generado una nueva contraseña temporal.')
        except User.DoesNotExist:
            messages.error(request, 'El usuario no existe.')

    return render(request, 'usuarios/recuperar_contrasena.html', {'nueva_contrasena': nueva_contrasena})
    
    




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

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all().select_related('perfil')
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})