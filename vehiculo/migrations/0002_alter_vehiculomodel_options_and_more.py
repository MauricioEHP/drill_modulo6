# Generated by Django 4.0.5 on 2023-07-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Puede visualizar_catalogo'),)},
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='categoria',
            field=models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='Particular', max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='marca',
            field=models.CharField(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='Ford', max_length=20),
        ),
    ]
