from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from ..models import Client, Bank
from django.shortcuts import render, redirect

"""
def list_banks(request):
    banks = Bank.objects.all()
    return render (request, 'banks.html', {'banks': banks})
"""
#equivalente a la funcion de arribba
class List_Banks(ListView):
    model = Bank
    template_name = 'banks.html'
    
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

##
class Create_Client(CreateView):
    model = Client
    # que campos recibe del metodo POST
    fields = ['name', 'dni','address', 'bank_id']
    #equivalente al return
    success_url = '/clientes/'

#VSTAS BASADAS EN CLASES
class Update_Client(UpdateView):
    model = Client
    # que campos recibe del metodo POST
    fields = ['name', 'dni','address', 'bank_id']
    #equivalente al return
    success_url = '/clientes/'


class Delete_Client(DeleteView):
    model = Client
    success_url = '/clientes/'   