from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.core.forms.empleadoForm import EmpleadoForm
from applications.core.models import Empleado
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class EmpleadoListView(PermissionMixin, ListViewMixin, ListView):
    model = Empleado
    template_name = 'core/empleado/list.html'
    permission_required = 'core.view_empleado'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is not None:
            self.query.add(Q(nombres__icontains=q) | Q(apellidos__icontains=q),  Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:empleado_create')
        return context
    
class EmpleadoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'core/empleado/form.html'
    permission_required = 'core.add_empleado'
    success_url = reverse_lazy('core:empleado_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Añadir empleado'
        context['back_url'] = self.success_url
        context['cancelar'] = 'Cancelar'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombres
        messages.success(self.request, f'Empleado {object} creado exitosamente')
        return response
    
class EmpleadoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'core/empleado/form.html'
    permission_required = 'core.change_empleado'
    success_url = reverse_lazy('core:empleado_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar empleado'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombres
        messages.success(self.request, f'Empleado {object} actualizado exitosamente')
        return response
    
class EmpleadoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Empleado
    template_name = 'fragments/delete.html'
    permission_required = 'core.delete_empleado'
    success_url = reverse_lazy('core:empleado_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object.nombres
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Empleado {self.object.nombres} eliminado exitosamente')
        return response
    

