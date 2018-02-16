from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from apps.cliente.models import Cliente
from apps.cliente.forms import FormCliente


class Lista_cliente(ListView):
	model = Cliente
	template_name="cliente/lista_cliente.html"
	context_object_name = 'clientes'
	
	

class Registrar_cliente(CreateView):
	model = Cliente
	form_class = FormCliente
	template_name = 'cliente/registrar_cliente.html'
	success_url = reverse_lazy ('lista_cliente')


class Detalle_Cliente(DetailView):
    model = Cliente
    template_name = 'cliente/detalle_cliente.html'


 	

def Cliente_edit(request, id_cliente):
	cliente= Cliente.objects.get(id=id_cliente)
	if request.method == 'GET':
		form = FormCliente(instance= cliente)
	else:
		form = FormCliente(request.POST, instance = cliente)
		if form.is_valid():
			form.save()
		return	redirect ('lista_cliente')
	return render (request, 'cliente/registrar_cliente.html', {'form':form})

#def Cliente_delete(request, id_cliente):
#	cliente= Cliente.objects.get(id=id_cliente)
#	if request.method == 'POST':
#		cliente.delete()
#		return redirect('lista_cliente')
#	return render (request, 'cliente/cliente_delete.html', {'cliente':cliente})

class Cliente_delete(DeleteView):
	model = Cliente
	template_name = 'cliente/cliente_delete.html'
	success_url = reverse_lazy('lista_cliente')