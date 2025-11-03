from django.db import models


class Proveedor(models.Model):
    """
    Modelo para la gestión de proveedores.
    Incluye campos para documentos requeridos (RUT y Cámara de Comercio).
    """
    nombre = models.CharField(max_length=200, verbose_name='Nombre del Proveedor')
    nit = models.CharField(max_length=20, unique=True, verbose_name='NIT')
    direccion = models.CharField(max_length=300, verbose_name='Dirección')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Email')
    
    # Documentos requeridos
    rut = models.FileField(
        upload_to='documentos/proveedores/rut/',
        verbose_name='RUT',
        help_text='Registro Único Tributario'
    )
    camara_comercio = models.FileField(
        upload_to='documentos/proveedores/camara_comercio/',
        verbose_name='Cámara de Comercio',
        help_text='Certificado de Cámara de Comercio'
    )
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.nombre} - {self.nit}"

