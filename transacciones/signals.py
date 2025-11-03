"""
Señales para manejar la integridad de datos cuando se eliminan o modifican transacciones.
Restaura stock y ajusta movimientos de caja automáticamente.
"""

from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.db import transaction as db_transaction

from .models import Venta, DetalleVenta, Compra, DetalleCompra
from core.models import TransaccionCaja


@receiver(pre_delete, sender=DetalleVenta)
def restaurar_stock_detalle_venta(sender, instance, **kwargs):
    """
    Restaura el stock cuando se elimina un detalle de venta.
    Esto ocurre al editar una venta y eliminar líneas, o al borrar la venta completa.
    """
    if instance.pk:  # Solo si el detalle ya existe en BD
        tipo_huevo = instance.tipo_huevo
        tipo_huevo.stock_cubetas += instance.cantidad_cubetas
        tipo_huevo.save(update_fields=['stock_cubetas'])


@receiver(post_delete, sender=Venta)
def ajustar_caja_venta_eliminada(sender, instance, **kwargs):
    """
    Elimina la transacción de caja asociada cuando se elimina una venta.
    El pre_delete de DetalleVenta ya restauró el stock.
    """
    # Eliminar el ingreso de caja asociado a esta venta
    TransaccionCaja.objects.filter(venta_id=instance.id).delete()


@receiver(pre_delete, sender=DetalleCompra)
def restaurar_stock_detalle_compra(sender, instance, **kwargs):
    """
    Resta el stock cuando se elimina un detalle de compra.
    (Revertir la adición de stock que se hizo al crear la compra)
    """
    if instance.pk:  # Solo si el detalle ya existe en BD
        tipo_huevo = instance.tipo_huevo
        # Al eliminar una compra, RESTAMOS el stock que se había agregado
        tipo_huevo.stock_cubetas -= instance.cantidad_cubetas
        tipo_huevo.save(update_fields=['stock_cubetas'])


@receiver(post_delete, sender=Compra)
def ajustar_caja_compra_eliminada(sender, instance, **kwargs):
    """
    Elimina la transacción de caja asociada cuando se elimina una compra.
    El pre_delete de DetalleCompra ya ajustó el stock.
    """
    # Eliminar el egreso de caja asociado a esta compra
    TransaccionCaja.objects.filter(compra_id=instance.id).delete()
