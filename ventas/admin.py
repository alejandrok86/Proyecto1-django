from django.contrib import admin
from .models import *

# Registrar nuestros modelos.

admin.site.register(Client)
admin.site.register(Bank)
