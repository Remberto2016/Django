from django.conf.urls import url, include
from apps.cliente.views import *


#from django.contrib.auth.views import logout
#from django.contrib.auth.decorators import login_required
urlpatterns = [
url(r'^cliente/$',Lista_cliente.as_view(), name='lista_cliente'),
url(r'^registrar/cliente/$',Registrar_cliente.as_view(), name='registrar_cliente'),
url(r'^cliente_detalle/(?P<pk>.+)/$',Detalle_Cliente.as_view(), name="detalle_cliente"),
url(r'^cliente/editar/(?P<id_cliente>\d+)/$', Cliente_edit, name='editar_cliente'),
#url(r'^cliente/eliminar/(?P<id_cliente>\d+)/$', Cliente_delete, name='eliminar_cliente'),
url(r'^cliente/eliminar/(?P<pk>.+)/$', Cliente_delete.as_view(), name='eliminar_cliente'),  


]