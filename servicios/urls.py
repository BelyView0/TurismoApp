from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index_usuario, name='index_admin'),
    path('', views.index_admin, name='index_usuario'),
    
    path('lugares/', views.lugar_list, name='lugar_list'),
    path('lugares/crear/', views.lugar_create, name='lugar_create'),
    path('lugares/<int:pk>/', views.lugar_detail, name='lugar_detail'),
    path('lugares/<int:pk>/editar/', views.lugar_update, name='lugar_update'),
    path('lugares/<int:pk>/eliminar/', views.lugar_delete, name='lugar_delete'),
    # URLS de hoteles
    path('hoteles/', views.hotel_list, name='hotel_list'),
    path('hoteles/crear/', views.hotel_create, name='hotel_create'),
    path('hoteles/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('hoteles/<int:pk>/editar/', views.hotel_update, name='hotel_update'),
    path('hoteles/<int:pk>/eliminar/', views.hotel_delete, name='hotel_delete'),
    # URLS de restaurantes
    path('restaurantes/', views.restaurante_list, name='restaurante_list'),
    path('restaurantes/crear/', views.restaurante_create, name='restaurante_create'),
    path('restaurantes/<int:pk>/', views.restaurante_detail, name='restaurante_detail'),
    path('restaurantes/<int:pk>/editar/', views.restaurante_update, name='restaurante_update'),
    path('restaurantes/<int:pk>/eliminar/', views.restaurante_delete, name='restaurante_delete'),

]

