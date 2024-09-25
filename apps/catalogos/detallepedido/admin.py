from django.contrib import admin
from apps.catalogos.detallepedido.models import DetallePedido

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','descripcion','cantidad','precio','total','producto']
