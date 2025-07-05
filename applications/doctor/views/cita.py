from django.contrib import messages
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.models import CitaMedica
from applications.doctor.forms.cita import CitaMedicaForm
from applications.security.components.mixin_crud import PermissionMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class CitaMedicaListView(PermissionMixin, ListView):
    model = CitaMedica
    template_name = 'doctor/cita/lista.html'
    context_object_name = 'citas'
    permission_required = 'view_citamedica'

    def get_queryset(self):
        return CitaMedica.objects.all().order_by('fecha', 'hora_cita')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:cita_create')
        return context

class CitaMedicaCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'doctor/cita/form.html'
    success_url = reverse_lazy('doctor:cita_list')
    permission_required = 'add_citamedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Registrar Cita'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                self.object = form.save()
                messages.success(self.request, "Cita médica creada correctamente.")
                return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error al crear la cita: {str(e)}")
            return super().form_invalid(form)

class CitaMedicaUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'doctor/cita/form.html'
    success_url = reverse_lazy('doctor:cita_list')
    permission_required = 'change_citamedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Cita'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                self.object = form.save()
                messages.success(self.request, "Cita médica actualizada correctamente.")
                return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Error al actualizar la cita: {str(e)}")
            return super().form_invalid(form)

class CitaMedicaDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = CitaMedica
    template_name = 'doctor/cita/confirm_delete.html'
    success_url = reverse_lazy('doctor:cita_list')
    permission_required = 'delete_citamedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Cita'
        context['description'] = f"¿Desea eliminar la cita de: {self.object.paciente}?"
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cita médica eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
