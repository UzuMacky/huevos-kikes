from django.db import models


class Cliente(models.Model):
    """
    Modelo para la gestión de clientes.
    Incluye campos de geolocalización para integración con Google Maps.
    """
    nombre = models.CharField(max_length=200, verbose_name='Nombre del Cliente')
    cedula_nit = models.CharField(max_length=20, unique=True, verbose_name='Cédula/NIT')
    direccion = models.CharField(max_length=300, verbose_name='Dirección')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Email')
    
    # Geolocalización
    latitud = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Latitud',
        help_text='Latitud de la ubicación del cliente'
    )
    longitud = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Longitud',
        help_text='Longitud de la ubicación del cliente'
    )
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.nombre} - {self.cedula_nit}"

