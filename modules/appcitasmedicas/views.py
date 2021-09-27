from modules.appcitasmedicas.models import Paciente
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):

    try:
        del request.session['id_paciente']
    except KeyError:
        pass

    return render(request, 'home.html')

def autenticar(request):

    #Authenticate user
    try:
        usuario = request.POST["username"]
        password = request.POST["password"]

        paciente = Paciente.objects.get(id=usuario, password=password)
        print(paciente)
        context = {"paciente" : paciente}
        request.session['id_paciente'] = paciente.id
    

    except ObjectDoesNotExist:
        context = {"mensaje" : "Paciente y/o contraseña inválidos."}
        return render(request, 'home.html', context)    

    return render(request, 'index.html', context)

def logout(request):

    try:
        del request.session['id_paciente']
    except KeyError:
        pass

    return render(request, 'home.html')