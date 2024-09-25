from django.contrib import admin
from apps.catalogos.pedido.models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','fecha','descripcion']

