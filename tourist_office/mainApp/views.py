# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.shortcuts import render
from mainApp.models import Lugar
from mainApp.models import Evento
from mainApp.models import Oficina
from mainApp.models import Categoria

# Create your views here.

def portada(request):
    lugares = Lugar.objects.all()
    eventos = Evento.objects.all()
    categorias = Categoria.objects.all()
    oficina = Oficina.objects.get(id_oficina = 1)
    return render(request, 'index.html', {'lugares':lugares, 'eventos':eventos, 'oficina': oficina, 'categorias':categorias})

def detalles(request, id_evento):
    evento = Evento.objects.get(id_evento = id_evento)
    categorias = Categoria.objects.all()
    return render(request, 'detalles.html', {'evento':evento, 'categorias':categorias})

def contacto(request):
    oficina = Oficina.objects.get(id_oficina = 1)
    categorias = Categoria.objects.all()
    return render(request, 'contacto.html',{'oficina':oficina, 'categorias':categorias})

def eventos_por_categoria(request, id_categoria):
    eventos = Evento.objects.filter(categoriaid_categoria = id_categoria)
    categoria = Categoria.objects.get(id_categoria = id_categoria)
    oficina = Oficina.objects.get(id_oficina = 1)
    categorias = Categoria.objects.all()
    return render(request, 'eventos.html',{'eventos':eventos, 'categoria':categoria, 'oficina':oficina,'categorias':categorias})
