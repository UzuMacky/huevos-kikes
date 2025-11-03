from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TransaccionCaja


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin para el modelo CustomUser."""
    pass


@admin.register(TransaccionCaja)
class TransaccionCajaAdmin(admin.ModelAdmin):
    """Admin para el modelo TransaccionCaja."""
    list_display = ['tipo', 'monto', 'fecha_hora', 'venta', 'compra']
    list_filter = ['tipo', 'fecha_hora']
    search_fields = ['descripcion']
    readonly_fields = ['fecha_hora']

