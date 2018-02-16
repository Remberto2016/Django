from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render 
from django.views.generic import TemplateView 

from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
#Importamos el formulario de autenticación de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from apps.usuario.forms import RegistroForm



class Index(TemplateView):
	template_name="usuario/index.html"

# Create your views here.
class Bienvenida(TemplateView):
	template_name="usuario/inicio.html"

class RegistroUsuario(CreateView):
	"""docstring for RegistroUsuario"""
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy("usuario:inicio")

    


class Login(FormView):
    #Establecemos la plantilla a utilizar
	template_name = "usuario/login.html"
    #Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
	form_class = AuthenticationForm
    #Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
	success_url =  reverse_lazy('usuario:inicio')

	
 
	def dispatch(self, request, *args, **kwargs):
        #Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
		if request.user.is_authenticated():
			return HttpResponseRedirect(self.get_success_url())
			userr =Login.objects.get(username=request.user)

        #Sino lo está entonces nos muestra la plantilla del login simplemente
		else:
			return super(Login, self).dispatch(request, *args, **kwargs)

			
 
	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(Login, self).form_valid(form)

class Usuario_detalle(DetailView):
    model = User
    template_name = "usuario/detalle_usuario.html"
		