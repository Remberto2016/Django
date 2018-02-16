from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from apps.cliente.models import Cliente
from apps.inventario.models import Articulo

# Create your models here.

class Pedido(models.Model):
	cod_cliente=models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
	id_articulo= models.ForeignKey(Articulo, null=True,blank=True, on_delete=models.CASCADE)
	fechapedido=models.DateField((""),default=date.today)
	fechaentrega=models.DateField((""),default=date.today)
	fechaenvio=models.DateField((""),default=date.today)
	destinatario=models.CharField(max_length=50)
	descripcion=models.TextField(blank=True, max_length=200)
	dirdestinatario=models.CharField(max_length=50)
	ciudaddestainatario=models.CharField(max_length=20)
	regiondestinatario=models.CharField(max_length=20)
	paisdestainatario = models.CharField(max_length=20)
	precio_unidad = models.FloatField(null=True, blank=True, default=None)
	cantidad = models.IntegerField()
	descuento = models.FloatField(null=True, blank=True, default=None)
	Sub_total = models.FloatField(null=True, blank=True, default=None)

	def __unicode__(self):
		return '%s %s' % (self.destinatario)
	def __str__(self):
		return '%s %s' % (self.destinatario)



