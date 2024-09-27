from django.contrib import admin
from django.urls import path
from ventas.views import list_clients, create_client, delete_client, update_client


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('ruta/', ), que es lo quiero que haga (controlador-vista)
    path('clientes/', list_clients, name='list_clients'),
    path('crear/cliente/', create_client, name='create_client'),
    path('delete/cliente/<id>', delete_client, name='delete_client'),
    path('update/cliente/<id>', update_client, name='update_client'),
]
