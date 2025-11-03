from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """Admin para el modelo Cliente."""
    list_display = ['nombre', 'cedula_nit', 'telefono', 'email', 'activo', 'fecha_registro']
    list_filter = ['activo', 'fecha_registro']
    search_fields = ['nombre', 'cedula_nit', 'email']
    readonly_fields = ['fecha_registro']

