from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Client(models.Model):
    # campos = tipo de datos models.CharField(max_length=200) para el caso de string
    name = models.CharField(max_length=200)
    # por defecto puede estar vacio
    dni = models.CharField(max_length=200, null=True)
    # por defecto si se deja vacio se completa con ese dato
    address = models.CharField(max_length=200, default="SIN DOMICILIO")
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    # borrado en cascada del banco
    bank_id = models.ForeignKey(Bank, null=True, on_delete=models.CASCADE)
    # bank_id = models.ManyToManyField(Bank)

    def __str__(self):
        # esta funcion cambia la visualizacion en la bd por el nombre cliente
        return self.name


"""
class Sale(models.Model):
    pass



class Caja(models.Model):
    number = models.CharField(max_length=200)


    #client_id = models.ForeignKey(Client) # otra forma de hacer ONE TO ONE
    # client_id = models.OneToOneField(Client)
    # one to one field (modelo cliente)
    # one to many
    # client_id = models.OneToManyField(Client) en verciones vieja se usa esa linea
    # pero en django 4 en adelante cambia a
    # client_id = models.ManyToOneRel(Client)
    # many to many
    #clients = models.ManyToManyField(Client)  # se agrega en un solo lado
    # crea una tabla intermedia
    def __str__(self):
        return self.number


class Factura(models.Model):
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number
"""
