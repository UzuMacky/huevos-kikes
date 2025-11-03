"""
Formularios para la app de transacciones (ventas y compras).
"""
from django import forms
from django.forms import inlineformset_factory
from .models import Venta, DetalleVenta, Compra, DetalleCompra


class VentaForm(forms.ModelForm):
    """Formulario para crear una venta."""
    
    class Meta:
        model = Venta
        fields = ['cliente']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }


class DetalleVentaForm(forms.ModelForm):
    """Formulario para los detalles de venta."""
    
    class Meta:
        model = DetalleVenta
        fields = ['tipo_huevo', 'cantidad_cubetas', 'precio_unitario_cubeta']
        widgets = {
            'tipo_huevo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_cubetas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'precio_unitario_cubeta': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
        }


# Formset para detalles de venta
DetalleVentaFormSet = inlineformset_factory(
    Venta,
    DetalleVenta,
    form=DetalleVentaForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True
)


class CompraForm(forms.ModelForm):
    """Formulario para crear una compra."""
    
    class Meta:
        model = Compra
        fields = ['proveedor', 'fecha_hora', 'medio_pago']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_hora': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'medio_pago': forms.Select(attrs={'class': 'form-control'}),
        }


class DetalleCompraForm(forms.ModelForm):
    """Formulario para los detalles de compra."""
    
    class Meta:
        model = DetalleCompra
        fields = ['tipo_huevo', 'cantidad_cubetas', 'precio_unitario_cubeta']
        widgets = {
            'tipo_huevo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad_cubetas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'precio_unitario_cubeta': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
        }


# Formset para detalles de compra
DetalleCompraFormSet = inlineformset_factory(
    Compra,
    DetalleCompra,
    form=DetalleCompraForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True
)
