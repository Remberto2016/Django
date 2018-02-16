from django import forms
from .models import Ventas, Detalleventa, Modo_pago, Factura
from django.core.exceptions import ValidationError


class Formventas(forms.ModelForm):
	class Meta:
		model = Ventas
		fields = [
				
				'cod_cliente', 
				'fechaventa',
				
		]
		labels = {
				
				'cod_cliente':'Cliente',
				'fechaventa':'Fecha',
				
		}
		
		widgets = {
				
				'cod_cliente':forms.TextInput(attrs={'class':'form-control'}),
				'fechaventa':forms.TextInput(attrs={'class':'form-control', "type":"date"}),
		}
class Formdetalleventa(forms.ModelForm):
	class Meta:
		model = Detalleventa
		fields = [
				
				'id_venta', 
				'id_articulo',
				'precio',
				'cantidad',
				'Sub_total',
		]
		labels =  {
				

				'id_venta':'Venta',
				'id_articulo':'Articulo',
				'precio':'Costo Unidad',
				'cantidad':'Cantidad',
				'Sub_total':'Total',
		}
		widgets = {
				
				'id_venta':forms.TextInput(attrs={'class':'form-control'}),
				'id_articulo':forms.TextInput(attrs={'class':'form-control'}),
				'precio':forms.TextInput(attrs={'class':'form-control'}),
				'cantidad':forms.TextInput(attrs={'class':'form-control'}),
				'Sub_total':forms.TextInput(attrs={'class':'form-control'}),
		}
class Formpago(forms.ModelForm):
	class Meta:
		model = Modo_pago
		fields = [				
				'nombre', 
				'descripcion',
		]
		labels =  {
				'nombre':'Tipo de Modo_pago',
				'descripcion':'descripcion',
			
		}
		widgets = {		
				'nombre':forms.TextInput(attrs={'class':'form-control'}),
				'descripcion':forms.TextInput(attrs={'class':'form-control'}),

		}
class Formfactura(forms.ModelForm):
	class Meta:
		model = Factura
		fields = [				
				'id_factura',
				'id_detalleventa', 
				'cod_cliente',
				'id_articulo',
				'fechafactura',
				'id_pago',
		]
		labels =  {
				'id_factura':'Venta',
				'id_detalleventa':'Detalle venta',
				'cod_cliente':'Cliente',
				'id_articulo':'Articulo',
				'fechafactura':'Fecha',
				'id_pago':'Modo de pago',

		}
		widgets = {		
				'id_factura':forms.TextInput(attrs={'class':'form-control'}),
				'id_detalleventa':forms.TextInput(attrs={'class':'form-control'}),
				'cod_cliente':forms.TextInput(attrs={'class':'form-control'}),
				'id_articulo':forms.TextInput(attrs={'class':'form-control'}),
				'fechaventa':forms.TextInput(attrs={'class':'form-control', "type":"date"}),
				'id_pago':forms.TextInput(attrs={'class':'form-control'}),


		}

			
				
