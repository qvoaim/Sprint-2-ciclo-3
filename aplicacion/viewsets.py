from rest_framework import viewsets
from . import models
from . import  serializers

class EntidadViewset(viewsets.ModelViewset):
    queryset=models.Entidad.objects.all()
    serializers_class=serializers.EntidadSerializer
    