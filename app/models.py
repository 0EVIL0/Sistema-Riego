from django.db import models

from django.db import models


class rol(models.Model):
 
    id =  models.AutoField(primary_key = True)
    nombre = models.CharField('nombre',max_length=40, null=False, blank=False) 
    descripcion = models.CharField('descripcion',max_length=80)


class Usuario(models.Model):
    id =  models.AutoField(primary_key = True)
    rol = models.ForeignKey(rol, on_delete=models.CASCADE, default=1)
    nombres = models.CharField('nombres', max_length=40, null=False, blank=False)
    Apellidos = models.CharField('Apellidos', max_length=30,  null=False, blank=False)
    Usuario = models.CharField('Usuario', max_length=60,  null=False, blank=False)
    Contrasena = models.CharField('Contrasena', max_length=30,  null=False, blank=False)
    telefono =  models.CharField('telefono', max_length=30,  null=False, blank=False)

class Auditoria(models.Model):
    id=   models.AutoField(primary_key = True)
    Descripcion = models.CharField('Descripcion', max_length=30, null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)

class Sensores(models.Model):
    id=  models.AutoField(primary_key = True)
    tipo_sensor=models.CharField('tipo_sensor',max_length=40, null=False, blank=False) 
    Descripcion_sensor= models.CharField('Descripcion_sensor',max_length=30, null=False, blank=False)

class registro(models.Model):
    codigo =   models.AutoField(primary_key = True)
    codigo_sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    registro_sensor =  models.CharField('registro', max_length=30, null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)

     


