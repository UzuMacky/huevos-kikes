from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Modelo de Usuario personalizado que hereda de AbstractUser.
    Por ahora no tiene campos adicionales, pero permite futuras extensiones.
    """
    pass

    def __str__(self):
        return self.username


class TransaccionCaja(models.Model):
    """
    Modelo para registrar todas las transacciones de caja (ingresos y egresos).
    """
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('egreso', 'Egreso'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True)
    
    # Referencias opcionales a ventas o compras
    venta = models.ForeignKey(
        'transacciones.Venta',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transacciones_caja'
    )
    compra = models.ForeignKey(
        'transacciones.Compra',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transacciones_caja'
    )

    class Meta:
        ordering = ['-fecha_hora']
        verbose_name = 'Transacción de Caja'
        verbose_name_plural = 'Transacciones de Caja'

    def __str__(self):
        return f"{self.get_tipo_display()} - ${self.monto} - {self.fecha_hora.strftime('%Y-%m-%d %H:%M')}"
