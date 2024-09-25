from django.db import models

from apps.catalogos.cliente.models import Cliente
from apps.catalogos.estado.models import Estado

"""
Pedidos
"""

class Pedido(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente,verbose_name='Cliente', on_delete=models.PROTECT)
    fecha = models.DateField(verbose_name='Fecha y Hora')
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    estado = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f"{self.codigo} - {self.fecha} - {self.descripcion}"
