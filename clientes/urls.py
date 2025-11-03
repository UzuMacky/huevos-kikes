"""
URLs para la app de clientes.
"""
from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView
)

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='list'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='detail'),
    path('crear/', ClienteCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='delete'),
]
