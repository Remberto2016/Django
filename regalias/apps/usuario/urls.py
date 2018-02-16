from django.conf.urls import url
from apps.usuario.views import *
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$',Index.as_view(), name='index'),
    url(r'^login/$',Login.as_view(), name='login'),
    url(r'^inicio/$',Bienvenida.as_view(), name='inicio'),
    url(r'^salir/$', logout, name="salir", kwargs={'next_page': '/'}),
    url(r'^registrar/$',RegistroUsuario.as_view(), name='registrar'),
    url(r'^usuario/detalle/(?P<pk>.+)$',Usuario_detalle.as_view(), name='detalle'),
]