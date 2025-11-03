from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from openpyxl import Workbook
from .models import TipoHuevo


class InventarioListView(LoginRequiredMixin, ListView):
    """
    Vista para listar el inventario de tipos de huevo.
    Incluye funcionalidad para exportar a Excel.
    """
    model = TipoHuevo
    template_name = 'inventario/inventario_list.html'
    context_object_name = 'tipos_huevo'
    login_url = 'core:login'

    def get(self, request, *args, **kwargs):
        """
        Verifica si se solicita exportar a Excel.
        Si es así, genera y retorna el archivo Excel.
        """
        if request.GET.get('export') == 'excel':
            return self.export_to_excel()
        
        return super().get(request, *args, **kwargs)

    def export_to_excel(self):
        """
        Genera un archivo Excel con los datos del inventario.
        """
        # Crear workbook y hoja
        wb = Workbook()
        ws = wb.active
        ws.title = "Inventario"

        # Encabezados
        headers = ['Tipo', 'Precio por Cubeta', 'Stock en Cubetas']
        ws.append(headers)

        # Datos
        tipos_huevo = TipoHuevo.objects.all()
        for tipo in tipos_huevo:
            ws.append([
                tipo.get_tipo_display(),
                float(tipo.precio_cubeta),
                tipo.stock_cubetas
            ])

        # Ajustar anchos de columna
        ws.column_dimensions['A'].width = 15
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 20

        # Crear respuesta HTTP
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=inventario_huevos.xlsx'
        
        wb.save(response)
        return response

