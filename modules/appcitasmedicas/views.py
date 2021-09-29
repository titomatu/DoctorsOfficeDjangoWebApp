from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):

    return render(request, 'home.html')
    
def login(request):

    return render(request, 'login.html')

def usuario(request):

    return render(request, 'usuario.html')

def agendamiento(request):

    return render(request, 'agendamiento.html')
    
def consultas(request):

    return render(request, 'consultas.html')