from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.core.models import GastoMensual
from applications.core.forms.gastoMensualForm import GastoMensualForm
from applications.security.components.mixin_crud import (
    ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
)


class GastoMensualListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/gastomensual/list.html'
    model = GastoMensual
    context_object_name = 'gastos'
    permission_required = 'view_gastomensual'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(observacion__icontains=q), Q.OR)
            self.query.add(Q(tipo_gasto__nombre__icontains=q), Q.OR)
        return self.model.objects.select_related('tipo_gasto').filter(self.query).order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:gastomensual_create')
        return context


class GastoMensualCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gastomensual/form.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'add_gastomensual'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Gasto Mensual'
        context['back_url'] = self.success_url
        return context


class GastoMensualUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gastomensual/form.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'change_gastomensual'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Gasto Mensual'
        context['back_url'] = self.success_url
        return context


class GastoMensualDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GastoMensual
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'delete_gastomensual'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Gasto Mensual'
        context['description'] = f"¿Desea eliminar el gasto del tipo: {self.object.tipo_gasto} del {self.object.fecha}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        gasto_info = str(self.object)
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar el gasto mensual: {gasto_info}.")
        return response
