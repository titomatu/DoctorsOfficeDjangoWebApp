from django.db import models

# Create your models here.

class Paciente(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, null=False)
    nombres= models.CharField(max_length=64,  null=False)
    apellidos = models.CharField(max_length=64, null=False)
    direccion = models.CharField(max_length=64, null=True)
    telefonos = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=64, null=True)
    password = models.CharField(max_length=8, null=False) 

    def __str__(self):
        return f"{self.nombres} - {self.apellidos}"


class Medico(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, null=False)
    nombres = models.CharField(max_length=64,  null=False)
    apellidos = models.CharField(max_length=64, null=False)
    direccion = models.CharField(max_length=64, null=True)
    telefonos = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=64, null=True)
    especialidad = models.CharField(max_length=64, null=True)
    password = models.CharField(max_length=8, null=False) 

    def __str__(self):
        return f"{self.nombres} - {self.apellidos}"

class Disponibilidad(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, null=False)
    medico = medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False)
    fecha = models.DateField(null= True)
    hora = models.TimeField(null= True)

    def __str__(self):
        return f"{self.medico} - {self.fecha} - {self.hora}"

class Cita(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, null=False)
    disponibilidad = models.ForeignKey(Disponibilidad, on_delete=models.CASCADE, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    lista_cancela = [('S', 'Si'), ('N', 'No')]
    cancelada = models.TextField(max_length=1, null=False, choices=lista_cancela)
    hora_cancelada = models.TimeField(null= True)

    def __str__(self):
        return f"{self.paciente} - {self.dosponibildad} "