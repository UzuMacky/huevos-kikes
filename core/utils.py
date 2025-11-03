"""
Funciones de utilidad para el manejo de la caja.
"""
from django.db.models import Sum
from .models import TransaccionCaja


def registrar_transaccion_caja(monto, tipo, venta_id=None, compra_id=None, descripcion=''):
    """
    Registra una transacción en la caja.
    
    Args:
        monto (Decimal): Monto de la transacción
        tipo (str): 'ingreso' o 'egreso'
        venta_id (int, optional): ID de la venta relacionada
        compra_id (int, optional): ID de la compra relacionada
        descripcion (str, optional): Descripción adicional de la transacción
    
    Returns:
        TransaccionCaja: La transacción creada
    """
    transaccion = TransaccionCaja.objects.create(
        tipo=tipo,
        monto=monto,
        venta_id=venta_id,
        compra_id=compra_id,
        descripcion=descripcion or f"{'Venta' if venta_id else 'Compra'} #{venta_id or compra_id}"
    )
    return transaccion


def get_saldo_actual():
    """
    Calcula el saldo actual en caja.
    
    Returns:
        Decimal: Saldo actual (ingresos - egresos)
    """
    ingresos = TransaccionCaja.objects.filter(tipo='ingreso').aggregate(
        total=Sum('monto')
    )['total'] or 0
    
    egresos = TransaccionCaja.objects.filter(tipo='egreso').aggregate(
        total=Sum('monto')
    )['total'] or 0
    
    return ingresos - egresos
