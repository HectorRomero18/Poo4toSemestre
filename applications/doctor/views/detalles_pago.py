import json
from decimal import Decimal

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from applications.doctor.forms.pago import DetallePagoForm
from applications.doctor.models import Pago, Atencion, DetallePago, ServiciosAdicionales
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class DetallePagoCreateView(PermissionMixin, CreateView, CreateViewMixin):
    model = DetallePago
    form_class = DetallePagoForm
    template_name = 'doctor/detalles_pago/form.html'
    permission_required = 'add_detallepago'
    success_url = reverse_lazy('doctor:pago_list')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Agregar Detalle de Pago'
        context['back_url'] = self.success_url
        context['det_form'] = DetallePagoForm()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Detalle Pago agregado correctamente')
        return response


class DetallePagoUpdateView(PermissionMixin, UpdateView, UpdateViewMixin):
    model = DetallePago
    form_class = DetallePagoForm
    template_name = 'doctor/detalles_pago/update.html'
    permission_required = 'change_detallepago'
    success_url = reverse_lazy('doctor:pago_list')

    def get_object(self, queryset=None):
        """Obtener el DetallePago basado en el ID del Pago"""
        pago_id = self.kwargs.get('pk')
        pago = get_object_or_404(Pago, pk=pago_id)
        servicio_default = ServiciosAdicionales.objects.first()

        if not servicio_default:
            raise Exception("No hay servicios adicionales disponibles para asignar al detalle.")

        
        # Intentar obtener el detalle, si no existe, crearlo
        detalle, created = DetallePago.objects.get_or_create(
            pago=pago,
            defaults={
                'cantidad': 1,
                'precio_unitario': Decimal('0.00'),
                'subtotal': Decimal('0.00'),
                'servicio_adicional': servicio_default,
            }
        )
        return detalle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar'
        context['back_url'] = self.success_url
        context['pago'] = self.object.pago 
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Detalle Pago actualizado correctamente')
        return response