from django.contrib import admin
from .models import Venta, DetalleVenta, Compra, DetalleCompra


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    """Admin para el modelo Venta."""
    list_display = ['id', 'cliente', 'usuario_vendedor', 'fecha_hora', 'total']
    list_filter = ['fecha_hora', 'usuario_vendedor']
    search_fields = ['cliente__nombre', 'cliente__cedula_nit']
    readonly_fields = ['fecha_hora']
    inlines = [DetalleVentaInline]


class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    """Admin para el modelo Compra."""
    list_display = ['id', 'proveedor', 'fecha_hora', 'medio_pago', 'total']
    list_filter = ['fecha_hora', 'medio_pago']
    search_fields = ['proveedor__nombre', 'proveedor__nit']
    inlines = [DetalleCompraInline]

