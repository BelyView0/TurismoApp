from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index_servicios'),
    path('lugares/', views.lugar_list, name='lugar_list'),
    path('lugares/crear/', views.lugar_create, name='lugar_create'),
    path('lugares/<int:pk>/', views.lugar_detail, name='lugar_detail'),
    path('lugares/<int:pk>/editar/', views.lugar_update, name='lugar_update'),
    path('lugares/<int:pk>/eliminar/', views.lugar_delete, name='lugar_delete'),
]