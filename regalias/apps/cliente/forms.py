from django import forms
from .models import Cliente
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
class FormCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
				'cod_cliente', 
				'ci', 
				'nombres',
				'apellidos', 
				'razon_social', 
				'direccion', 
				'correo', 
				'telefono',
				'sexo',
				'fecha',
				'ciudad',
				'telefono_fijo',
				'nacionalidad',
				'provincia',
				'pais',
		]
		labels = {
				'cod_cliente':'Codigo de cliente',
				'ci':'Cedula de identidad',
				'nombres':'Nombre cliente',
				'apellidos':'Apellidos cliente',
				'razon_social':'Razon social',
				'direccion':'Direccion',
				'correo':'Correo',
				'telefono':'Telefono',
				'sexo':'Sexo',
				'fecha':'Fecha',
				'ciudad':'Ciudad',
				'telefono_fijo': 'Telefono Fijo',
				'nacionalidad':'Nacionalidad',
				'provincia':'Estado o Provincia',
				'pais':'Pais',
		}
		widgets = {
				'cod_cliente': forms.TextInput(attrs={'class':'form-control','autofocus':'true'}),
				'ci':forms.TextInput(attrs={'class':'form-control', 'autofocus':'true'}),
				'nombres':forms.TextInput(attrs={'class':'form-control'}),
				'apellidos':forms.TextInput(attrs={'class':'form-control'}),
				'razon_social':forms.TextInput(attrs={'class':'form-control'}),
				'direccion':forms.TextInput(attrs={'class':'form-control'}),
				'correo':forms.TextInput(attrs={'class':'form-control'}),
				'telefono':forms.TextInput(attrs={'class':'form-control'}),
				'sexo':forms.Select(attrs={'class':'form-control'}),
				'fecha':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
				'ciudad':forms.TextInput(attrs={'class':'form-control'}),
				'telefono_fijo':forms.TextInput(attrs={'class':'form-control'}),
				'nacionalidad':forms.TextInput(attrs={'class':'form-control'}),
				'provincia':forms.TextInput(attrs={'class':'form-control'}),
				'pais':forms.TextInput(attrs={'class':'form-control'}),
		}	

