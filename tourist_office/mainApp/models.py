# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categoria'


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    puntuacion = models.IntegerField()
    precio = models.FloatField()
    oficinaid_oficina = models.ForeignKey('Oficina', models.DO_NOTHING, db_column='Oficinaid_oficina')  # Field name made lowercase.
    categoriaid_categoria = models.ForeignKey('Categoria', models.DO_NOTHING, db_column='Categoriaid_categoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evento'


class Lugar(models.Model):
    id_lugar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lugar'


class Oficina(models.Model):
    id_oficina = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    lugarid_lugar = models.ForeignKey('Lugar', models.DO_NOTHING, db_column='Lugarid_lugar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'oficina'
