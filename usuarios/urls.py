from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('usuario/', views.index_usuario, name='index_usuario'),
    path('admin/', views.index_admin, name='index_admin'),
    path('lista-usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
]
