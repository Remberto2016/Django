from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class RegistroForm(UserCreationForm):
	"""docstring for RegistroForm"""
	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
				'is_superuser',

				
				

			]
		labels = {
					'username':'Nombre de usuario',
					'first_name':'Nombre',
					'last_name':'Apellidos',
					'email':'Correo',
					'is_superuser': 'Super usuario',
					
			}
		widgets={
					'username':forms.TextInput(attrs={'class': 'input-field'}),
					'first_name':forms.TextInput(attrs={'class': 'input-field'}),
					'last_name':forms.TextInput(attrs={'class': 'input-field'}),
					'email':forms.TextInput(attrs={'class': 'input-field', 'type':'email'}),
					'is_superuser':forms.TextInput(attrs={'class': 'input-field'}),
					
					


		}
