"""
URLs para la app de proveedores.
"""
from django.urls import path
from .views import (
    ProveedorListView,
    ProveedorDetailView,
    ProveedorCreateView,
    ProveedorUpdateView,
    ProveedorDeleteView
)

app_name = 'proveedores'

urlpatterns = [
    path('', ProveedorListView.as_view(), name='list'),
    path('<int:pk>/', ProveedorDetailView.as_view(), name='detail'),
    path('crear/', ProveedorCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', ProveedorUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='delete'),
]
