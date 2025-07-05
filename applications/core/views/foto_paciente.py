from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.core.models import FotoPaciente
from applications.core.forms.fotoPacienteForm import FotoPacienteForm
from applications.security.components.mixin_crud import (
    ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
)

class FotoPacienteListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/fotopaciente/list.html'
    model = FotoPaciente
    context_object_name = 'fotos'
    permission_required = 'view_fotopaciente'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(paciente__nombres__icontains=q), Q.OR)
            self.query.add(Q(descripcion__icontains=q), Q.OR)
        return self.model.objects.select_related('paciente').filter(self.query).order_by('-fecha_subida')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:fotopaciente_create')
        return context


class FotoPacienteCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = FotoPaciente
    form_class = FotoPacienteForm
    template_name = 'core/fotopaciente/form.html'
    success_url = reverse_lazy('core:fotopaciente_list')
    permission_required = 'add_fotopaciente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Subir Foto de Paciente'
        context['back_url'] = self.success_url
        return context


class FotoPacienteUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = FotoPaciente
    form_class = FotoPacienteForm
    template_name = 'core/fotopaciente/form.html'
    success_url = reverse_lazy('core:fotopaciente_list')
    permission_required = 'change_fotopaciente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Foto de Paciente'
        context['back_url'] = self.success_url
        return context


class FotoPacienteDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = FotoPaciente
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:fotopaciente_list')
    permission_required = 'delete_fotopaciente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Foto de Paciente'
        context['description'] = f"¿Desea eliminar la foto subida por el paciente: {self.object.paciente}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        paciente_nombre = str(self.object.paciente)
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar la foto del paciente: {paciente_nombre}.")
        return response
