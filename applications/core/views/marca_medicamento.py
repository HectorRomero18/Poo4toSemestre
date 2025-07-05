from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.core.models import MarcaMedicamento
from applications.core.forms.marcaMedicamentoForm import MarcaMedicamentoForm
from applications.security.components.mixin_crud import (
    ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
)

class MarcaMedicamentoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/marcamedicamento/list.html'
    model = MarcaMedicamento
    context_object_name = 'marcas'
    permission_required = 'view_marcamedicamento'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(nombre__icontains=q), Q.OR)
            self.query.add(Q(descripcion__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:marcamedicamento_create')
        return context

class MarcaMedicamentoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = 'core/marcamedicamento/form.html'
    success_url = reverse_lazy('core:marcamedicamento_list')
    permission_required = 'add_marcamedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Marca de Medicamento'
        context['back_url'] = self.success_url
        context['title'] = 'Crear Marca de Medicamento'
        return context

class MarcaMedicamentoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = 'core/marcamedicamento/form.html'
    success_url = reverse_lazy('core:marcamedicamento_list')
    permission_required = 'change_marcamedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Marca de Medicamento'
        context['back_url'] = self.success_url
        context['title'] = 'Actualizar Marca de Medicamento'
        return context

class MarcaMedicamentoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = MarcaMedicamento
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:marcamedicamento_list')
    permission_required = 'delete_marcamedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Marca de Medicamento'
        context['description'] = f"¿Desea eliminar la marca: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar la marca de medicamento: {nombre}.")
        return response
