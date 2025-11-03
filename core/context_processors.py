"""
Context processors para el proyecto.
Permite acceder a variables de configuración en todos los templates.
"""
from django.conf import settings


def google_maps_api_key(request):
    """
    Agrega la API Key de Google Maps al contexto de todos los templates.
    """
    return {
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY
    }
