from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.core.models import Medicamento
from applications.core.forms.medicamentoForm import MedicamentoForm
from applications.security.components.mixin_crud import (
    ListViewMixin, CreateViewMixin, UpdateViewMixin,
    DeleteViewMixin, PermissionMixin
)


class MedicamentoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/medicamento/list.html'
    model = Medicamento
    context_object_name = 'medicamentos'
    permission_required = 'view_medicamento'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(nombre__icontains=q), Q(descripcion__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:medicamento_create')
        return context


class MedicamentoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('core:medicamento_list')
    permission_required = 'add_medicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Medicamento'
        context['back_url'] = self.success_url
        return context


class MedicamentoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('core:medicamento_list')
    permission_required = 'change_medicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Medicamento'
        context['back_url'] = self.success_url
        return context


class MedicamentoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Medicamento
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:medicamento_list')
    permission_required = 'delete_medicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Medicamento'
        context['description'] = f"¿Desea eliminar el medicamento: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar el medicamento: {nombre}.")
        return response
