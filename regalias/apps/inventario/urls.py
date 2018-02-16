from django.conf.urls import url, include
from apps.inventario.views import *




urlpatterns = [
    
  url(r'^inventario/$',Lista_inventario.as_view(), name='lista_inventario'),
  url(r'^inventario/registrar/proveedor/$',Registrar_proveedor.as_view(), name='registrar_proveedor'),
  url(r'^inventario/proveedor/$',Lista_proveedor.as_view(), name='lista_proveedor'),
  url(r'^inventario/proveedor/editar/(?P<id_proveedor>\d+)/$', Proveedor_edit, name='editar_proveedor'),
  url(r'^inventario/proveedor/eliminar/(?P<id_proveedor>\d+)/$', Proveedor_delete, name='eliminar_proveedor'),
  url(r'^inventario/proveedor/detalle/(?P<pk>.+)/$', Detalle_proveedor.as_view(), name='detalle_proveedor'),
  url(r'^inventario/producto/$',Lista_producto.as_view(), name='lista_producto'),
  url(r'^inventario/producto/registrar/$',Registrar_producto.as_view(), name='registrar_producto'),
  url(r'^inventario/producto/editar/(?P<id_producto>\d+)/$', Producto_edit, name='editar_producto'),
  url(r'^inventario/producto/detalle/(?P<pk>.+)/$', Detalle_producto.as_view(), name='detalle_producto'),

]