from rest_framework import viewsets
from . import models
from . import serializers

class UsuariosViewset(viewsets.ModelViewSet):
    queryset=models.Usuarios.objects.all()
    serializer_class=serializers.UsuariosSerializer

class LibrosViewset(viewsets.ModelViewSet):
    queryset=models.Libros.objects.all()
    serializer_class=serializers.LibrosSerializer