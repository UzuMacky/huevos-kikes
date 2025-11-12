from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TransaccionCaja
from .utils import get_saldo_actual
from .forms import LoginFormWithCaptcha


class CustomLoginView(LoginView):
    """Vista personalizada para el login con captcha."""
    template_name = 'core/login.html'
    form_class = LoginFormWithCaptcha
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """Vista personalizada para el logout."""
    next_page = 'core:login'


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Vista del Dashboard principal que muestra:
    - Saldo actual en caja
    - Últimas 10 transacciones de ingreso
    - Últimas 10 transacciones de egreso
    """
    template_name = 'core/dashboard.html'
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener saldo actual
        context['saldo_actual'] = get_saldo_actual()
        
        # Últimas 10 transacciones de ingreso
        context['ingresos_recientes'] = TransaccionCaja.objects.filter(
            tipo='ingreso'
        )[:10]
        
        # Últimas 10 transacciones de egreso
        context['egresos_recientes'] = TransaccionCaja.objects.filter(
            tipo='egreso'
        )[:10]
        
        # Totales
        context['total_ingresos'] = sum(
            t.monto for t in TransaccionCaja.objects.filter(tipo='ingreso')
        )
        context['total_egresos'] = sum(
            t.monto for t in TransaccionCaja.objects.filter(tipo='egreso')
        )
        
        return context

