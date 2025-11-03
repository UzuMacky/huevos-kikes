"""
Formularios para la app de clientes.
"""
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    """
    Formulario para crear/editar clientes.
    """
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'cedula_nit', 'direccion', 'telefono', 'email', 'latitud', 'longitud', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
            'cedula_nit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula o NIT'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'latitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_latitud',
                'placeholder': 'Latitud',
                'step': 'any'
            }),
            'longitud': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_longitud',
                'placeholder': 'Longitud',
                'step': 'any'
            }),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
