from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from apps.pedidos.models import Pedido 
from apps.pedidos.forms import FormPedido
from django.views.generic.edit import FormView


# Create your views here.
class Lista_pedido(ListView):
	model=Pedido
	template_name="pedido/lista_pedido.html"
	context_object_name = 'pedidos' 

class Registrar_pedido(CreateView):
	model = Pedido
	form_class=FormPedido
	template_name = 'pedido/registrar_pedido.html'
	success_url = reverse_lazy ('lista_pedido')
	
class Detalle_Pedido(DetailView):
	model = Pedido
	template_name = 'pedido/detalle_pedido.html'

class Actualizar_pedido(UpdateView):
	model = Pedido
	form_class = FormPedido
	template_name = 'pedido/registrar_pedido.html'
	success_url = reverse_lazy ('lista_pedido')
	
	



