from django.conf.urls import url, include
from apps.pedidos.views import *

#from django.contrib.auth.views import logout
#from django.contrib.auth.decorators import login_required
urlpatterns = [
    
    url(r'^pedido/$',Lista_pedido.as_view(), name='lista_pedido'),
    url(r'^registrar/pedido/$',Registrar_pedido.as_view(), name='registrar_pedido'),
    url(r'^pedido/actualizar/(?P<pk>.+)/$' ,Actualizar_pedido.as_view(), name='actulizar_pedido'),
    url(r'^pedido_detalle/(?P<pk>.+)/$' ,Detalle_Pedido.as_view(), name='detalle_pedido'),
]