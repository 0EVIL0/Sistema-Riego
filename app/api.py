from .serializers import *
from rest_framework import viewsets,permissions
from .models import *

class rolViewSet(viewsets.ModelViewSet):
    queryset=rol.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=rolSerealizer
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=UsuariosSerealizer

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset=Auditoria.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=AuditoriaSerealizer

class SensoresViewSet(viewsets.ModelViewSet):
    queryset=Sensores.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=SensoresSerealizer

class RegistroViewSet(viewsets.ModelViewSet):
    queryset=registro.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=RegistroSerealizer
