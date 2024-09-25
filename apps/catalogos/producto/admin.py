from django.contrib import admin
from apps.catalogos.producto.models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','codigoColor','precio','cantidad']
    ordering = ['codigo']  # ordena de manera ascedente los registros
