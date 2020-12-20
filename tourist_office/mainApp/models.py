# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")
    foto = models.ImageField(upload_to = 'mainApp/img/categorias', verbose_name="Imagen")

    class Meta:
        managed = False
        db_table = 'categoria'
    
    def __str__(self):
        return self.nombre

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")
    foto = models.ImageField(upload_to = 'mainApp/img/eventos', verbose_name="Imagen")
    puntuacion = models.IntegerField(verbose_name="Popularidad")
    precio = models.FloatField()
    oficinaid_oficina = models.ForeignKey('Oficina', models.DO_NOTHING, db_column='Oficinaid_oficina')  # Field name made lowercase.
    categoriaid_categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoriaid_categoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evento'

    def __str__(self):
        return self.nombre


class Lugar(models.Model):
    id_lugar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    foto = models.ImageField(upload_to = 'mainApp/img/lugares', verbose_name="Imagen")
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")

    class Meta:
        managed = False
        db_table = 'lugar'

    def __str__(self):
        return self.nombre


class Oficina(models.Model):
    id_oficina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, verbose_name="Dirección")
    email = models.CharField(max_length=255, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=255, verbose_name="Teléfono")
    descripcion = models.CharField(max_length=255, verbose_name="Descripción")
    foto = models.ImageField(upload_to = 'mainApp/img/oficinas', verbose_name="Imagen")
    lugarid_lugar = models.ForeignKey('Lugar', models.DO_NOTHING, db_column='Lugarid_lugar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oficina'

    def __str__(self):
        return self.nombre
