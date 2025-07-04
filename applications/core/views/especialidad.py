from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.core.forms.especialidadForm import EspecialidadForm
from applications.core.models import Especialidad
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class EspecialidadListView(PermissionMixin, ListViewMixin, ListView):
    model = Especialidad
    template_name = 'core/especialidad/list.html'
    permission_required = 'core.view_especialidad'
    context_object_name = 'especialidades'
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is not None:
            self.query.add(Q(nombre__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:especialidad_create')
        return context
    
class EspecialidadCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'core/especialidad/form.html'
    permission_required = 'core.add_especialidad'
    success_url = reverse_lazy('core:especialidad_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Añadir especialidad'
        context['back_url'] = self.success_url
        context['cancelar'] = 'Cancelar'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombre
        messages.success(self.request, f'Especialidad {object} creada exitosamente')
        return response
    
class EspecialidadUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'core/especialidad/form.html'
    permission_required = 'core.change_especialidad'
    success_url = reverse_lazy('core:especialidad_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar especialidad'
        context['back_url'] = self.success_url
        return context

class EspecialidadDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Especialidad
    template_name = 'fragments/delete.html'
    permission_required = 'core.delete_especialidad'
    success_url = reverse_lazy('core:especialidad_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, f'Especialidad eliminada exitosamente')
        return super().delete(request, *args, **kwargs)
