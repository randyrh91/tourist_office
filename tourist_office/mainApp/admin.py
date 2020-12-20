# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.contrib import admin
from .models import Categoria, Evento, Lugar, Oficina

# Register your models here.
class AdminLugares(admin.ModelAdmin):
    search_fields = ("nombre",)

class AdminOficina(admin.ModelAdmin):
    search_fields = ("nombre",)

class AdminEventos(admin.ModelAdmin):
    search_fields = ("nombre",)

class AdminCategorias(admin.ModelAdmin):
    search_fields = ("nombre",)

admin.site.register(Lugar, AdminLugares)
admin.site.register(Oficina, AdminOficina)
admin.site.register(Evento, AdminEventos)
admin.site.register(Categoria, AdminCategorias)
