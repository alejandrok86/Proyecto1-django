from django.contrib import admin
from django.urls import path
from ventas.views.banks import List_Banks
from ventas.views.clients import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', List_Clients.as_view(), name='list_clients'),
    path('crear/cliente/', Create_Client.as_view(), name='create_client'),
    path('delete/cliente/<id>', Delete_Client.as_view(), name='delete_client'),
    path('update/cliente/<id>', Update_Client.as_view(), name='update_client'),
    path('bancos/', List_Banks.as_view(), name='list_banks'),
]

