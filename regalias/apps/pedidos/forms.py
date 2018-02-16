from django import forms
from .models import Pedido
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class FormPedido(forms.ModelForm):
	class Meta:
		model = Pedido
		
		fields = [
		'cod_cliente',
		'id_articulo', 
		'fechapedido',
		'fechaentrega', 
		'fechaenvio',
		'descripcion', 
		'destinatario', 
		'dirdestinatario', 
		'ciudaddestainatario',
		'regiondestinatario',
		'paisdestainatario',
		'precio_unidad',
		'cantidad',
		'descuento',
		'Sub_total',

		]

		labels = {
		'cod_cliente':'Nombre de Cliente',
		'id_articulo':'Articulo',
		'fechapedido':'Fecha de Pedido',
		'fechaentrega':'Fecha de Entrega',
		'fechaenvio':'Fecha de Envio',
		'descripcion':'Descripcion',
		'destinatario':'Destinatario',
		'dirdestinatario':'Direccion de Destinatario',
		'ciudaddestainatario':'Ciudad de Destino',
		'regiondestinatario':'Region de Destino',
		'paisdestainatario':'Pais de Destino',
		'precio_unidad':'Precio Unitario',
		'cantidad':'Cantidad',
		'descuento':'Descuento',
		'Sub_total':'Total',

		}
		widgets = {

		'cod_cliente':forms.Select(attrs={'class': 'form-control'}), 
		'id_articulo':forms.Select(attrs={'class': 'form-control'}), 
		'fechapedido':forms.TextInput(attrs={'class': 'form-control',  "type":"date"}),
		'fechaentrega':forms.TextInput(attrs={'class': 'form-control', "type":"date"}), 
		'fechaenvio':forms.TextInput(attrs={'class': 'form-control', "type":"date"}),
		'descripcion':forms.Textarea(attrs={'class': 'form-control', 'rows':'2'}),
		'destinatario':forms.TextInput(attrs={'class': 'form-control'}), 
		'dirdestinatario':forms.TextInput(attrs={'class': 'form-control'}), 
		'ciudaddestainatario':forms.TextInput(attrs={'class': 'form-control'}),
		'regiondestinatario':forms.TextInput(attrs={'class': 'form-control'}),
		'paisdestainatario':forms.TextInput(attrs={'class': 'form-control'}),
		'precio_unidad':forms.TextInput(attrs={'class': 'form-control'}),
		'cantidad':forms.TextInput(attrs={'class': 'form-control'}),
		'descuento':forms.TextInput(attrs={'class': 'form-control'}),
		'Sub_total':forms.TextInput(attrs={'class': 'form-control'}),
		}
		
