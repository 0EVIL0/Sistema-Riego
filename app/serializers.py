from rest_framework import serializers
from .models import *

class rolSerealizer(serializers.ModelSerializer):
    class Meta:
        model=rol
        fields="__all__"

class UsuariosSerealizer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields="__all__"

class AuditoriaSerealizer(serializers.ModelSerializer):
    class Meta:
        model=Auditoria
        fields="__all__"

class SensoresSerealizer(serializers.ModelSerializer):
    class Meta:
        model=Sensores
        fields="__all__"
class RegistroSerealizer(serializers.ModelSerializer):
    class Meta:
        model=registro
        fields="__all__"