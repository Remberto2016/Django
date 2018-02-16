from django.contrib import admin
from .models import Ventas, Detalleventa, Modo_pago, Factura
# Register your models here.
admin.site.register(Ventas)
admin.site.register(Detalleventa)
admin.site.register(Modo_pago)
admin.site.register(Factura)