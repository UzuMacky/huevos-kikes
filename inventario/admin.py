from django.contrib import admin
from .models import TipoHuevo


@admin.register(TipoHuevo)
class TipoHuevoAdmin(admin.ModelAdmin):
    """Admin para el modelo TipoHuevo."""
    list_display = ['tipo', 'precio_cubeta', 'stock_cubetas']
    list_editable = ['precio_cubeta', 'stock_cubetas']

