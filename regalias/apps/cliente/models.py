from __future__ import unicode_literals
from django.db import models

from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.
def validate_ci(value):
    if len(str(value)) != 10 and len(str(value)) != 8 and len(str(value)) != 7:
        raise ValidationError(u'%s No es un Cedula de Identidad'% value)
    return validate_ci


GENERO = (('', 'Seleccione Genero'),
		 ('Masculino','Masculino'), 
		 ('Femenino', 'Femenino'),)


class Cliente(models.Model):
	cod_cliente=models.PositiveIntegerField(unique=True)
	ci = models.CharField(validators=[validate_ci], max_length=10,unique=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=100)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=15)
	correo = models.EmailField(blank=True)
	razon_social = models.CharField(max_length=50)
	sexo = models.CharField(choices = GENERO, max_length=10)
	fecha=models.DateField((''),default=date.today)
	ciudad = models.CharField(max_length=15)
	telefono_fijo = models.CharField(max_length=15)
	nacionalidad = models.CharField(max_length=15)
	provincia = models.CharField(max_length=15)
	pais = models.CharField(max_length=15)
	def __unicode__(self):
		return '%s %s' % (self.nombres, self.apellidos)
	def __str__(self):
		return '%s %s' % (self.nombres, self.apellidos)


