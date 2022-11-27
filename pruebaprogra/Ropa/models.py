from django.db import models

# Create your models here.

class Ropa(models.Model):
    tipo_de_ropa = models.CharField(max_length=20)
    genero = models.CharField(max_length=15)
    talla = models.CharField(max_length=5)
    temporada = models.CharField(max_length=20)
    estilo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    cantidad = models.CharField(max_length=20)