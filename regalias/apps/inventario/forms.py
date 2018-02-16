from django import forms
from .models import Proveedor, Articulo
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class FormProveedor(forms.ModelForm):
	class Meta:
		model = Proveedor
		fields = [
				'id',
				'ci',
				'nit', 
				'nombres',
				'apellidos', 
				'sexo',
				'razon_social', 
				'direccion', 
				'telefono',
				'correo', 
				'fecha',
		]
		labels = {
				'id': 'ID',
				'nit': 'NIT',
				'ci':'Cedula de identidad',
				'nombres':'Nombre cliente',
				'apellidos':'Apellidos cliente',
				'sexo':'Sexo',
				'razon_social':'Razon social',
				'direccion':'Direccion',
				'telefono':'Telefono',
				'correo':'Correo',
				'fecha':'Fecha',
		}
		
		widgets = {
				'ci':forms.TextInput(attrs={'class':'form-control'}),
				'nit':forms.TextInput(attrs={'class':'form-control'}),
				'nombres':forms.TextInput(attrs={'class':'form-control'}),
				'apellidos':forms.TextInput(attrs={'class':'form-control'}),
				'sexo':forms.Select(attrs={'class':'form-control'}),
				'razon_social':forms.TextInput(attrs={'class':'form-control'}),
				'direccion':forms.TextInput(attrs={'class':'form-control'}),
				'telefono':forms.TextInput(attrs={'class':'form-control'}),
				'correo':forms.TextInput(attrs={'class':'form-control'}),
				'fecha':forms.TextInput(attrs={'class':'form-control', "type":"date"}),
		}	
class FormProducto(forms.ModelForm):
	class Meta:
		model = Articulo
		fields = [

				'nombre',
				'cod_categoria', 
				'descripcion',
				'costo_unitario', 
				'costo_venta', 
				'stock_actual',
				'proveedor', 
		]
		labels = {
				'nombre':'Nombre cliente',
				'cod_categoria':'Categoria',
				'descripcion':'Descripcion',
				'costo_unitario':'Costo Unidad',
				'costo_venta':'Costo Venta',
				'stock_actual':'Stock Actual',
				'proveedor':'Proveedor',
		}
		
		widgets = {
				'nombre':forms.TextInput(attrs={'class':'form-control'}),
				'cod_categoria':forms.TextInput(attrs={'class':'form-control'}),
				'descripcion':forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
				'costo_unitario':forms.TextInput(attrs={'class':'form-control'}),
				'costo_venta':forms.TextInput(attrs={'class':'form-control'}),
				'stock_actual':forms.TextInput(attrs={'class':'form-control'}),
				'proveedor':forms.Select(attrs={'class':'form-control'}),

		}	