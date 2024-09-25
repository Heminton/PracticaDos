#from django.contrib import admin
#from apps.catalogos.municipio.models import Municipio

#@admin.register(Municipio)
#class MunicipioAdmin(admin.ModelAdmin):
#    search_fields = ['id','nombre']
#    list_display = ['codigo','nombre','departamento']
#    ordering = ['codigo']  # ordena de manera ascedente los registros









from django.contrib import admin
from apps.catalogos.municipio.models import Municipio

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['codigo', 'nombre', 'mostrar_departamento']
    ordering = ['codigo']  # ordena de manera ascedente los registros

    def mostrar_departamento(self, obj):
        return obj.departamento.nombre  # Solo mostramos el nombre del departamento

    mostrar_departamento.short_description = 'Departamento'  # Etiqueta para el campo en el admin

