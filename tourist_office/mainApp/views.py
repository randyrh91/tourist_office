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
