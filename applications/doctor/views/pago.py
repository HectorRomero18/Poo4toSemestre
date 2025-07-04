import json
from decimal import Decimal

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from applications.doctor.forms.pago import PagoForm
from django.shortcuts import render
from applications.doctor.models import Pago, Atencion
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, \
    PermissionMixin, UpdateViewMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class PagoListView(PermissionMixin, ListViewMixin, ListView):
    model = Pago
    template_name = 'doctor/pago/pago_list.html'
    context_object_name = 'pagos'
    permission_required = 'view_pago'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is not None:
            self.query.add(Q(atencion__paciente__nombres__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:pago_create')
        return context
    
# Crud Transaccional para crear un pago
class PagoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'doctor/pago/pago_form.html'
    permission_required = 'add_pago'
    success_url = reverse_lazy('doctor:detalle_pago_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Crear Pago'
        context['back_url'] = self.success_url
        context['atenciones'] = Atencion.objects.all()
        return context

    @method_decorator(csrf_exempt)  # Solo si no estás usando CSRF correctamente en el fetch
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            nombre_pagador = request.POST.get('nombre_pagador')
            monto_total = request.POST.get('monto_total')
            metodo_pago = request.POST.get('metodo_pago')
            referencia_externa = request.POST.get('referencia_externa')
            observaciones = request.POST.get('observaciones')
            atencion_id = request.POST.get('atencion')
            fecha_pago = request.POST.get('fecha_pago')
            evidencia_archivo = request.FILES.get('evidencia_pago')
            estado = 'pendiente'

            if not all([nombre_pagador, monto_total, metodo_pago]):
                return JsonResponse({'msg': 'Faltan datos obligatorios'}, status=400)

            atencion = None
            if atencion_id:
                try:
                    atencion = Atencion.objects.get(id=atencion_id)
                except Atencion.DoesNotExist:
                    return JsonResponse({'msg': 'Atención no encontrada'}, status=404)
            
            if evidencia_archivo:
                estado = 'pagado'

            pago = Pago.objects.create(
                nombre_pagador=nombre_pagador,
                monto_total=monto_total,
                metodo_pago=metodo_pago,
                referencia_externa=referencia_externa,
                observaciones=observaciones,
                evidencia_pago=evidencia_archivo,
                atencion=atencion,
                fecha_pago = fecha_pago,
                estado = estado
            )

            return JsonResponse({'msg': 'Pago creado correctamente', 'id': pago.id}, status=200)

        except Exception as e:
            return JsonResponse({'msg': str(e)}, status=500)

class PagoUpdateView(PermissionMixin, UpdateView, UpdateViewMixin):
    model = Pago
    permission_required = 'change_pago'
    form_class = PagoForm
    success_url = reverse_lazy('doctor:pago_list')
    template_name = 'doctor/pago/pago_form_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar'
        context['back_url'] = self.success_url
        context['pago'] = self.get_object()  # Objeto pago para el template
        context['atenciones'] = Atencion.objects.all()  # Lista de atenciones
        return context
    
    def get(self, request, *args, **kwargs):
        """Maneja las peticiones GET - muestra el formulario"""
        self.object = self.get_object()
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        """Maneja las peticiones POST - procesa el formulario via AJAX"""
        self.object = self.get_object()
        
        try:
            # Obtener los datos del formulario
            nombre_pagador = request.POST.get('nombre_pagador')
            monto_total = request.POST.get('monto_total')
            metodo_pago = request.POST.get('metodo_pago')
            fecha_pago = request.POST.get('fecha_pago')
            referencia_externa = request.POST.get('referencia_externa')
            atencion_id = request.POST.get('atencion')
            observaciones = request.POST.get('observaciones')
            evidencia_pago = request.FILES.get('evidencia_pago')
            estado = 'pendiente'
            
            # Validaciones básicas
            if not nombre_pagador or not monto_total or not metodo_pago or not fecha_pago:
                return JsonResponse({
                    'success': False,
                    'msg': 'Los campos marcados con * son obligatorios'
                }, status=400)
            
            if evidencia_pago:
                estado = 'pagado'
            
            # Actualizar el objeto pago
            self.object.nombre_pagador = nombre_pagador
            self.object.monto_total = float(monto_total)
            self.object.metodo_pago = metodo_pago
            self.object.fecha_pago = fecha_pago
            self.object.referencia_externa = referencia_externa or ''
            self.object.observaciones = observaciones or ''
            self.object.estado = estado
            
            # Actualizar atención si se proporcionó
            if atencion_id:
                try:
                    atencion = Atencion.objects.get(id=atencion_id)
                    self.object.atencion = atencion
                except Atencion.DoesNotExist:
                    pass
            
            # Actualizar evidencia si se proporcionó nueva
            if evidencia_pago:
                self.object.evidencia_pago = evidencia_pago
            
            # Guardar los cambios
            self.object.save()
            
            # Mensaje de éxito
            messages.success(request, f'Pago actualizado correctamente')
            
            return JsonResponse({
                'success': True,
                'msg': 'Pago actualizado correctamente',
                'redirect_url': str(self.success_url)
            })
            
        except ValueError as e:
            return JsonResponse({
                'success': False,
                'msg': 'Error en el formato de los datos. Verifique el monto.'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'msg': f'Error al actualizar el pago: {str(e)}'
            }, status=500)
    
    def form_valid(self, form):
        """Método de respaldo para formularios tradicionales"""
        response = super().form_valid(form)
        messages.success(self.request, f'Pago editado correctamente')
        return response



class PagoDeleteView(PermissionMixin, DeleteView, DeleteViewMixin):
    model = Pago
    permission_required = 'delete_pago'
    template_name = 'doctor/pago_confirm_delete.html'
    success_url = reverse_lazy('doctor:pago_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description'] = 'Estas seguro de eliminar este registro?'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Pago eliminado correctamente')
        return response