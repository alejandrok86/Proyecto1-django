from django.shortcuts import render
from ..models import Client, Bank
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView,UpdateView, DeleteView


#Basadas en funciones
"""
def list_clients(request):
    clients = Client.objects.all()
    banks = Bank.objects.all()
    # return render('nombre archivo html', )
    return render(request, 'clients.html', {'clients': clients, 'banks': banks})
"""
# create con vistas basadas en clases
class List_Clients(ListView):
    model = Client
    template_name = 'clients.html'

"""
def create_client(request):
   # client = request.
    name = request.POST["name"]
    dni = request.POST["dni"]
    address = request.POST["address"]
    bank_id = request.POST["bank_id"]
    bank = Bank.objects.get(pk=bank_id)
    email = request.POST["email"]
    phone = request.POST["phone"]
    # instanciar el objeto
    client = Client(name=name, dni=dni, bank_id=bank, address=address,
                    email=email, phone=phone)
    # el metodo guardar  en la base
    client.save()
    return redirect('/clientes/')
"""
# esta funcion busca el objeto

## Basa en clases
class Create_Client(CreateView):
    model = Client
    # que campos recibe del metodo POST
    fields = ['name', 'dni','address', 'bank_id', 'email', 'phone']
    #equivalente al return
    success_url = '/clientes/'

"""
def detail(request, id):
    client = Client.objects.get(pk=id)
    bank = Bank.objects.get(id=client.bank_id)
"""

# delete

"""
def delete_client(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('/clientes/')
"""
## Basa en clases
class Delete_Client(DeleteView):
    model = Client
    success_url = '/clientes/'  
# update

"""
def update_client(request, id):
    # buscar el objeto
    client = Client.objects.get(pk=id)
    name = request.POST["name"]
    dni = request.POST["dni"]
    address = request.POST["address"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    bank_id = request.POST["bank_id"]
    ####recupero el objeto buscando por id
    bank = Bank.objects.get(pk=id)
    # actualizando los campos (seteo)
    client.name = name
    client.dni = dni
    client.address = address
    client.email = email
    client.phone = phone
    client.bank_id = bank
    # guardo los nuevos datos
    client.save()
    # rediciono a clientes
    return redirect('/clientes/')
"""
## Basa en clases
class Update_Client(UpdateView):
    model = Client
    # que campos recibe del metodo POST
    fields = ['name', 'dni','address', 'bank_id','email', 'phone']
    #equivalente al return
    success_url = '/clientes/'