#from django.contrib import admin

#from apps.catalogos.almacen.models import Almacen

#@admin.register(Almacen)
#class AlmacenAdmin(admin.ModelAdmin):
 #   search_fields = ['id','nombre']
  #  list_display = ['codigo','nombre','telefono','direccion','email','url','municipio']











from django.contrib import admin
from apps.catalogos.almacen.models import Almacen

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['codigo', 'nombre', 'telefono', 'direccion', 'email', 'url', 'mostrar_municipio']

    def mostrar_municipio(self, obj):
        return obj.municipio.nombre  # Solo mostramos el nombre del municipio

    mostrar_municipio.short_description = 'Municipio'  # Etiqueta para el campo en el admin




