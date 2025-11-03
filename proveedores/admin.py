from django.contrib import admin
from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    """Admin para el modelo Proveedor."""
    list_display = ['nombre', 'nit', 'telefono', 'email', 'activo', 'fecha_registro']
    list_filter = ['activo', 'fecha_registro']
    search_fields = ['nombre', 'nit', 'email']
    readonly_fields = ['fecha_registro']

