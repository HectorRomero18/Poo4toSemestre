from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db import transaction
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.doctor.models import HorarioAtencion
from applications.doctor.forms.horario import HorarioAtencionForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin

class HorarioAtencionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/horario/lista.html'
    model = HorarioAtencion
    context_object_name = 'horarios'
    permission_required = 'view_horarioatencion'

    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = self.model.objects.all()
        if q:
            queryset = queryset.filter(dia_semana__icontains=q)
        return queryset.order_by('dia_semana', 'hora_inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:horario_create')
        return context

class HorarioAtencionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = HorarioAtencion
    template_name = 'doctor/horario/form.html'
    form_class = HorarioAtencionForm
    success_url = reverse_lazy('doctor:horarios_list')
    permission_required = 'add_horarioatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Registrar Horario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                self.object = form.save()
                messages.success(self.request, "Horario registrado correctamente.")
                return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error al registrar el horario: {str(e)}")
            return super().form_invalid(form)

class HorarioAtencionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = HorarioAtencion
    template_name = 'doctor/horario/form.html'
    form_class = HorarioAtencionForm
    success_url = reverse_lazy('doctor:horarios_list')
    permission_required = 'change_horarioatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Horario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                self.object = form.save()
                messages.success(self.request, "Horario actualizado correctamente.")
                return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error al actualizar el horario: {str(e)}")
            return super().form_invalid(form)

class HorarioAtencionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = HorarioAtencion
    template_name = 'doctor/delete.html'
    success_url = reverse_lazy('doctor:horarios_list')
    permission_required = 'delete_horarioatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Horario'
        context['description'] = f"¿Desea eliminar el horario de: {self.object.dia_semana}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Horario eliminado correctamente.")
        return response