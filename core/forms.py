"""
Formularios para la app core.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class LoginFormWithCaptcha(AuthenticationForm):
    """
    Formulario de login personalizado con captcha.
    Hereda de AuthenticationForm para mantener toda la lógica de autenticación de Django.
    """
    captcha = CaptchaField(
        label='Verificación de seguridad',
        help_text='Ingrese los caracteres que ve en la imagen',
        error_messages={
            'invalid': 'El código de verificación es incorrecto. Inténtelo de nuevo.',
            'required': 'Por favor ingrese el código de verificación.',
        }
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clases Bootstrap a los campos
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Usuario',
            'autofocus': True
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['captcha'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ingrese el código'
        })
