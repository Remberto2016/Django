# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20180124_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='sexo',
            field=models.CharField(choices=[('', 'SELEcCIONE GENERO'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10),
        ),
    ]
