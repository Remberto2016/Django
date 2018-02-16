# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-09 21:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('cod_categoria', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('costo_unitario', models.FloatField(blank=True, default=None, null=True)),
                ('costo_venta', models.FloatField(blank=True, default=None, null=True)),
                ('stock_actual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_e', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('costo_u', models.FloatField(blank=True, default=None, null=True)),
                ('costo_t', models.FloatField(blank=True, default=None, null=True)),
                ('factura', models.IntegerField()),
                ('saldo', models.IntegerField()),
                ('articulo_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=10)),
                ('razon_social', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(blank=True, max_length=254)),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Salidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_s', models.DateField()),
                ('descripcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('costo_venta', models.FloatField(blank=True, default=None, null=True)),
                ('articulo_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Articulo')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Proveedor'),
        ),
    ]
