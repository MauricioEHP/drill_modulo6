# Generated by Django 4.0.5 on 2023-07-18 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0004_alter_vehiculomodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Puede visualizar_catalogo'), ('add_vehiculo', 'Agregar Vehículo'))},
        ),
    ]
