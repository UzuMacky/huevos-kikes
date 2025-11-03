"""
URLs para la app de inventario.
"""
from django.urls import path
from .views import InventarioListView

app_name = 'inventario'

urlpatterns = [
    path('', InventarioListView.as_view(), name='list'),
]
