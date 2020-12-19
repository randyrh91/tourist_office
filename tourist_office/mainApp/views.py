from django.http import request
from django.shortcuts import render
#from mainApp.models import *

# Create your views here.


def portada(request):
    #lugares = Lugar.objects.all()
    return render(request, 'index.html')
