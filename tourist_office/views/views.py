from django.http import HttpResponse
from django.shortcuts import render
from tourist_office.entity.Persona import Persona

# Metodos

# saludo/


def saludo(request):
    return HttpResponse("Hola, primera pagina con django")


def despedida(request):
    return HttpResponse("Hasta luego")


def dame_fecha(request, agno):
    return HttpResponse("los años son " + str(agno))


def saludo_plantilla(request, nombre):
    p = Persona(nombre, "Reyna")
    return render(request, "home.html", {"persona": p})
