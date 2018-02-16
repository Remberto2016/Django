from django.db import models
from apps.cliente.models import Cliente
from apps.inventario.models import Articulo
from datetime import date
#from .models import 
class Ventas(models.Model):
	id_venta=models.AutoField(primary_key=True)
	cod_cliente=models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	fechaventa=models.DateField(("date"),default=date.today)
	

	def __int__(self):
		return self.cod_cliente

class Detalleventa(models.Model):
	id_detalleventa=models.AutoField(primary_key=True)
	id_venta=models.ForeignKey(Ventas, null=True, blank=True, on_delete=models.CASCADE)
	id_articulo= models.ForeignKey(Articulo, null=True,blank=True, on_delete=models.CASCADE)
	precio = models.FloatField(null=True, blank=True, default=None)
	cantidad = models.IntegerField()
	Sub_total = models.FloatField(null=True, blank=True, default=None)

	def __int__(self):
		return self.cod_cliente


class Modo_pago(models.Model):
	id_pago=models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=20)
	descripcion=models.CharField(max_length=300)
	def __str__(self):
		return self.nombre


class Factura(models.Model):
	id_factura=models.AutoField(primary_key=True)
	id_detalleventa=models.ForeignKey(Detalleventa, null=True, blank=True, on_delete=models.CASCADE)
	cod_cliente=models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	id_articulo= models.ForeignKey(Articulo, null=True,blank=True, on_delete=models.CASCADE)
	fechafactura=models.DateField(("date"),default=date.today)
	id_pago=models.ForeignKey(Modo_pago, null=True, blank=True, on_delete=models.CASCADE)


	




