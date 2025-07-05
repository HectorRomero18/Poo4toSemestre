from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.core.models import TipoGasto
from applications.core.forms.tipoGastoForm import TipoGastoForm
from applications.security.components.mixin_crud import (
    ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
)

class TipoGastoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/tipogasto/list.html'
    model = TipoGasto
    context_object_name = 'tipos'
    permission_required = 'view_tipogasto'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(nombre__icontains=q), Q.OR)
            self.query.add(Q(descripcion__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:tipogasto_create')
        return context

class TipoGastoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'core/tipogasto/form.html'
    success_url = reverse_lazy('core:tipogasto_list')
    permission_required = 'add_tipogasto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Tipo de Gasto'
        context['back_url'] = self.success_url
        return context

class TipoGastoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'core/tipogasto/form.html'
    success_url = reverse_lazy('core:tipogasto_list')
    permission_required = 'change_tipogasto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Tipo de Gasto'
        context['back_url'] = self.success_url
        return context

class TipoGastoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = TipoGasto
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:tipogasto_list')
    permission_required = 'delete_tipogasto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Tipo de Gasto'
        context['description'] = f"¿Desea eliminar el tipo de gasto: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        tipo_nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar el tipo de gasto: {tipo_nombre}.")
        return response
