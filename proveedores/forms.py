"""
Formularios para la app de proveedores.
"""
from django import forms
from django.core.exceptions import ValidationError
from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    """
    Formulario para crear/editar proveedores.
    Incluye validación para asegurar que los archivos RUT y Cámara de Comercio se suban.
    """
    
    class Meta:
        model = Proveedor
        fields = ['nombre', 'nit', 'direccion', 'telefono', 'email', 'rut', 'camara_comercio', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'nit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIT'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'rut': forms.FileInput(attrs={'class': 'form-control'}),
            'camara_comercio': forms.FileInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        """
        Validación personalizada para asegurar que los archivos requeridos se hayan subido.
        """
        cleaned_data = super().clean()
        rut = cleaned_data.get('rut')
        camara_comercio = cleaned_data.get('camara_comercio')

        # Si estamos creando un nuevo proveedor (no hay instance.pk)
        if not self.instance.pk:
            if not rut:
                raise ValidationError({
                    'rut': 'Debe subir el archivo RUT.'
                })
            if not camara_comercio:
                raise ValidationError({
                    'camara_comercio': 'Debe subir el certificado de Cámara de Comercio.'
                })
        
        return cleaned_data
