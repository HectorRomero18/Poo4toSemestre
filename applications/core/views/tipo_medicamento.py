from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.core.models import TipoMedicamento
from applications.core.forms.tipoMedicamentoForm import TipoMedicamentoForm
from applications.security.components.mixin_crud import ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin

class TipoMedicamentoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/tipomedicamento/list.html'
    model = TipoMedicamento
    context_object_name = 'tipos'
    permission_required = 'view_tipomedicamento'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(nombre__icontains=q), Q.OR)
            self.query.add(Q(descripcion__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:tipomedicamento_create')
        return context

class TipoMedicamentoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = 'core/tipomedicamento/form.html'
    success_url = reverse_lazy('core:tipomedicamento_list')
    permission_required = 'add_tipomedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Tipo de Medicamento'
        context['back_url'] = self.success_url
        return context

class TipoMedicamentoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = 'core/tipomedicamento/form.html'
    success_url = reverse_lazy('core:tipomedicamento_list')
    permission_required = 'change_tipomedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Tipo de Medicamento'
        context['back_url'] = self.success_url
        return context

class TipoMedicamentoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = TipoMedicamento
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:tipomedicamento_list')
    permission_required = 'delete_tipomedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Tipo de Medicamento'
        context['description'] = f"¿Desea eliminar el tipo de medicamento: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        tipo_nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar el tipo de medicamento: {tipo_nombre}.")
        return response
