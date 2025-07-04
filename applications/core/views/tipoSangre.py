
from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.core.forms.tipoSangreForm import TipoSangreForm
from applications.core.models import TipoSangre
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class TipoSangreListView(PermissionMixin, ListViewMixin, ListView):
    model = TipoSangre
    template_name = 'core/tipoSangre/list.html'
    permission_required = 'core.view_tiposangre'
    context_object_name = 'tiposangre'
    
    def get_queryset(self):
        q = self.request.GET.get('q')

        if q is not None:
            self.query.add(Q(tipo__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:tipoSangre_create')
        return context
    
class TipoSangreCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = 'core/tipoSangre/form.html'
    permission_required = 'core.add_tiposangre'
    success_url = reverse_lazy('core:tipoSangre_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Añadir tipo de sangre'
        context['back_url'] = self.success_url
        context['cancelar'] = 'Cancelar'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.tipo
        messages.success(self.request, f'Tipo de sangre {object} creado exitosamente')
        return response

class TipoSangreUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = 'core/tipoSangre/form.html'
    permission_required = 'core.change_tiposangre'
    success_url = reverse_lazy('core:tipoSangre_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar tipo de sangre'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.tipo
        messages.success(self.request, f'Tipo de sangre {object} actualizado exitosamente')
        return response
    
class TipoSangreDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = TipoSangre
    template_name = 'fragments/delete.html'
    permission_required = 'core.delete_tiposangre'
    success_url = reverse_lazy('core:tipoSangre_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar tipo de sangre'
        context['back_url'] = self.success_url
        context['description'] = '¿Estás seguro de elimina ?'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.tipo
        messages.success(self.request, f'Tipo de sangre {object} eliminado exitosamente')
        return response