from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)

class Libros(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=300)
    autor=models.CharField(max_length=100)
    precio=models.CharField(max_length=30)