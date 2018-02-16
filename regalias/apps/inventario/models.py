from django.db import models
from datetime import date

# Create your models here.
GENERO = (('Masculino','Masculino'),
	('Femenino', 'Femenino'),)

class Proveedor(models.Model):
	ci=models.CharField(max_length=10, unique=True)
	nit=models.CharField(max_length=15, unique=True) 
	nombres=models.CharField(max_length=20)
	apellidos=models.CharField(max_length=20)
	sexo = models.CharField(choices = GENERO, max_length=10)
	razon_social=models.CharField(max_length=100)
	direccion=models.CharField(max_length=100)
	telefono=models.CharField(max_length=15)
	correo=models.EmailField(blank=True)
	fecha=models.DateField(("date"),default=date.today)


	def __str__(self):
		return self.nombres
		

class Articulo(models.Model):
	nombre= models.CharField(max_length=10)
	cod_categoria= models.CharField(max_length=50)
	descripcion = models.CharField(max_length=200)
	costo_unitario = models.FloatField(null=True, blank=True, default=None)
	costo_venta= models.FloatField(null=True, blank=True, default=None)
	stock_actual=models.IntegerField()
	proveedor=models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre

class Salidas(models.Model):
	fecha_s = models.DateField()
	descripcion=models.CharField(max_length=200)
	cantidad = models.IntegerField()
	costo_venta= models.FloatField(null=True, blank=True, default=None)
	articulo_id = models.ForeignKey(Articulo, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.descripcion

class Entradas(models.Model):
	fecha_e= models.DateField()
	descripcion=models.CharField(max_length=200)
	cantidad = models.IntegerField()
	costo_u= models.FloatField(null=True, blank=True, default=None)
	costo_t= models.FloatField(null=True, blank=True, default=None)
	factura= models.IntegerField()
	saldo = models.IntegerField()
	articulo_id = models.ForeignKey(Articulo, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.descripcion

