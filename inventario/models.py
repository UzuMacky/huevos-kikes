from django.db import models


class TipoHuevo(models.Model):
    """
    Modelo para gestionar los tipos de huevo en el inventario.
    Incluye precio por cubeta y stock actual.
    """
    TIPO_CHOICES = [
        ('A', 'A'),
        ('AA', 'AA'),
        ('AAA', 'AAA'),
    ]

    tipo = models.CharField(
        max_length=3,
        choices=TIPO_CHOICES,
        unique=True,
        verbose_name='Tipo de Huevo'
    )
    precio_cubeta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio por Cubeta'
    )
    stock_cubetas = models.PositiveIntegerField(
        default=0,
        verbose_name='Stock en Cubetas'
    )

    class Meta:
        ordering = ['tipo']
        verbose_name = 'Tipo de Huevo'
        verbose_name_plural = 'Tipos de Huevo'

    def __str__(self):
        return f"Huevo {self.tipo} - ${self.precio_cubeta} - Stock: {self.stock_cubetas}"

