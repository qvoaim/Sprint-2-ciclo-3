from dataclasses import field
from rest_framework import serializers
from .models import Usuarios
from .models import Libros

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields='__all__'

class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libros
        fields='__all__'