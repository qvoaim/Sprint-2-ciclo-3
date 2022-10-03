from django.db import models

class Entidad(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)

# Create your models here.
