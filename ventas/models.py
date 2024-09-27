from django.db import models


class Client(models.Model):
    # campos = tipo de datos models.CharField(max_length=200) para el caso de string
    name = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        # esta funcion cambia la visualizacion en la bd por el nombre cliente
        return self.name
