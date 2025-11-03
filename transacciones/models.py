from django.db import models
from django.conf import settings
from clientes.models import Cliente
from proveedores.models import Proveedor
from inventario.models import TipoHuevo


class Venta(models.Model):
    """
    Modelo para registrar las ventas realizadas.
    """
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='ventas',
        verbose_name='Cliente'
    )
    usuario_vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='ventas_realizadas',
        verbose_name='Vendedor'
    )
    fecha_hora = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Total'
    )

    class Meta:
        ordering = ['-fecha_hora']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre} - ${self.total}"


class DetalleVenta(models.Model):
    """
    Modelo para los detalles de cada venta (líneas de venta).
    """
    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE,
        related_name='detalles',
        verbose_name='Venta'
    )
    tipo_huevo = models.ForeignKey(
        TipoHuevo,
        on_delete=models.PROTECT,
        verbose_name='Tipo de Huevo'
    )
    cantidad_cubetas = models.PositiveIntegerField(verbose_name='Cantidad de Cubetas')
    precio_unitario_cubeta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio Unitario'
    )

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'

    def __str__(self):
        return f"{self.tipo_huevo.tipo} x {self.cantidad_cubetas}"

    @property
    def subtotal(self):
        """Calcula el subtotal de esta línea de detalle."""
        return self.cantidad_cubetas * self.precio_unitario_cubeta


class Compra(models.Model):
    """
    Modelo para registrar las compras realizadas a proveedores.
    """
    MEDIO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
    ]

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        related_name='compras',
        verbose_name='Proveedor'
    )
    fecha_hora = models.DateTimeField(verbose_name='Fecha y Hora')
    medio_pago = models.CharField(
        max_length=20,
        choices=MEDIO_PAGO_CHOICES,
        verbose_name='Medio de Pago'
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Total'
    )

    class Meta:
        ordering = ['-fecha_hora']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        return f"Compra #{self.id} - {self.proveedor.nombre} - ${self.total}"


class DetalleCompra(models.Model):
    """
    Modelo para los detalles de cada compra (líneas de compra).
    """
    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name='detalles',
        verbose_name='Compra'
    )
    tipo_huevo = models.ForeignKey(
        TipoHuevo,
        on_delete=models.PROTECT,
        verbose_name='Tipo de Huevo'
    )
    cantidad_cubetas = models.PositiveIntegerField(verbose_name='Cantidad de Cubetas')
    precio_unitario_cubeta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio Unitario'
    )

    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compra'

    def __str__(self):
        return f"{self.tipo_huevo.tipo} x {self.cantidad_cubetas}"

    @property
    def subtotal(self):
        """Calcula el subtotal de esta línea de detalle."""
        return self.cantidad_cubetas * self.precio_unitario_cubeta

