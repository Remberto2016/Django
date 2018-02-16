from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.inventario.models import Articulo, Proveedor
from apps.inventario.forms import FormProveedor, FormProducto

# Create your views here.
class Lista_inventario(ListView):

	model=Articulo
	template_name="inventario/lista_inventario.html"
	context_object_name = 'articulos'

class Registrar_proveedor(CreateView):
	model = Proveedor
	form_class = FormProveedor
	template_name = 'inventario/registrar_proveedor.html'
	success_url = reverse_lazy ('lista_proveedor')

class Detalle_proveedor(DetailView):
	model = Proveedor
	template_name = 'inventario/detalle_proveedor.html'


class Lista_proveedor(ListView):
	model=Proveedor
	template_name="inventario/proveedor.html"
	context_object_name = 'proveedor'

def Proveedor_edit(request, id_proveedor):
	proveedor= Proveedor.objects.get(id=id_proveedor)
	if request.method == 'GET':
		form = FormProveedor(instance= proveedor)
	else:
		form = FormProveedor(request.POST, instance = proveedor)
		if form.is_valid():
			form.save()
		return	redirect ('lista_proveedor')
	return render (request, 'inventario/registrar_proveedor.html', {'form':form})

def Proveedor_delete(request, id_proveedor):
	proveedor= Proveedor.objects.get(id=id_proveedor)
	if request.method == 'POST':
		proveedor.delete()
		return redirect('lista_proveedor')
	return render (request, 'inventario/proveedor_delete.html', {'proveedor':proveedor})

#-----------------------------------------

class Lista_producto(ListView):
	model=Articulo
	template_name="producto/Lista_producto.html"
	context_object_name = 'productos'

class Registrar_producto(CreateView):
	model = Articulo
	form_class = FormProducto
	template_name = 'producto/registrar_producto.html'
	success_url = reverse_lazy ('lista_producto')

class Detalle_producto(DetailView):
	model = Articulo
	template_name = 'producto/detalle_producto.html'

def Producto_edit(request, id_producto):
	producto= Articulo.objects.get(id=id_producto)
	if request.method == 'GET':
		form = FormProducto(instance= producto)
	else:
		form = FormProducto(request.POST, instance = producto)
		if form.is_valid():
			form.save()
		return	redirect ('lista_producto')
	return render (request, 'producto/registrar_producto.html', {'form':form})