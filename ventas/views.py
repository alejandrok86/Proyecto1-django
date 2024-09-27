from django.shortcuts import render
from .models import Client
# from django.http import HttpResponse
from django.shortcuts import render, redirect


def list_clients(request):
    clients = Client.objects.all()
    # return render('nombre archivo html', )
    return render(request, 'index.html', {'clients': clients})

# create


def create_client(request):
   # client = request.
    name = request.POST["name"]
    dni = request.POST["dni"]
    address = request.POST["address"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    # instanciar el objeto
    client = Client(name=name, dni=dni, address=address,
                    email=email, phone=phone)
    # el metodo guardar para  en la base
    client.save()
    return redirect('/clientes/')

# delete


def delete_client(request, id):
    client = Client.objects.get(pk=id)
    client.delete()
    return redirect('/clientes/')

# update


def update_client(request, id):
    # buscar el objeto
    client = Client.objects.get(pk=id)
    name = request.POST["name"]
    dni = request.POST["dni"]
    address = request.POST["address"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    # actualizando los campos (seteo)
    client.name = name
    client.dni = dni
    client.address = address
    client.email = email
    client.phone = phone
    # guardo los nuevos datos
    client.save()
    # rediciono a clientes
    return redirect('/clientes/')
