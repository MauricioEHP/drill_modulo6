from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class VehiculoModel(models.Model):
    Marcas_op = (
        ('Fiat','Fiat'),
        ('Chevrolet','Chevrolet'),
        ('Ford','Ford'),
        ('Toyota','Toyota'),
    )

    Categorias_op = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga','Carga'),
    )
    
    marca = models.CharField( max_length = 20, choices= Marcas_op, default= 'Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField( max_length=50)
    serial_motor = models.CharField( max_length=50)
    categoria = models.CharField( max_length=50, choices= Categorias_op, default= 'Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ("visualizar_catalogo","Puede visualizar_catalogo"),
            ("add_vehiculo","Agregar Vehículo"),
        )  

def __str__(self):
        return self.marca

ver_addgrupo, _ = Group.objects.get_or_create(name='ver_addgrupo')
Gvisualizar, _ = Group.objects.get_or_create(name='Gvisualizar')

permiso_visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo')
permiso_add_vehiculo = Permission.objects.get(codename='add_vehiculo')

ver_addgrupo.permissions.add(permiso_visualizar_catalogo, permiso_add_vehiculo)
Gvisualizar.permissions.add(permiso_visualizar_catalogo)
# Crear grupos.

    #Group.objects.create(name='Gvisualizar')
    #Gvisualizar = Group.permissions.add('visualizar_catalogo', 'add_vehiculo')