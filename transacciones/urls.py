"""
URLs para la app de transacciones (ventas y compras).
"""
from django.urls import path
from .views import (
    VentaListView, VentaDetailView, VentaCreateView, VentaUpdateView,
    CompraListView, CompraDetailView, CompraCreateView, CompraUpdateView,
    generar_factura_pdf
)

app_name = 'transacciones'

urlpatterns = [
    # Ventas
    path('ventas/', VentaListView.as_view(), name='ventas_list'),
    path('ventas/<int:pk>/', VentaDetailView.as_view(), name='venta_detail'),
    path('ventas/crear/', VentaCreateView.as_view(), name='venta_create'),
    path('ventas/<int:pk>/editar/', VentaUpdateView.as_view(), name='venta_update'),
    path('ventas/<int:pk>/pdf/', generar_factura_pdf, name='venta_pdf'),
    
    # Compras
    path('compras/', CompraListView.as_view(), name='compras_list'),
    path('compras/<int:pk>/', CompraDetailView.as_view(), name='compra_detail'),
    path('compras/crear/', CompraCreateView.as_view(), name='compra_create'),
    path('compras/<int:pk>/editar/', CompraUpdateView.as_view(), name='compra_update'),
]
