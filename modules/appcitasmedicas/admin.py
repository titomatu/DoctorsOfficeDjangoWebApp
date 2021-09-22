from django.contrib import admin

# Register your models here.
from modules.appcitasmedicas.models import *
admin.site.register(Pacientes)
admin.site.register(Medicos)
admin.site.register(Disponibilidad)
admin.site.register(Citas)