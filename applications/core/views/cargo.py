from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.core.forms.cargoForm import CargoForm
from applications.core.models import Cargo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class CargoListView(PermissionMixin, ListViewMixin, ListView):
    model = Cargo
    template_name = 'core/cargo/list.html'
    permission_required = 'core.view_cargo'
    context_object_name = 'cargos'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is not None:
            self.query.add(Q(nombre__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:cargo_create')
        return context
    
class CargoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'core/cargo/form.html'
    permission_required = 'core.add_cargo'
    success_url = reverse_lazy('core:cargo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Añadir cargo'
        context['back_url'] = self.success_url
        context['cancelar'] = 'Cancelar'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombre
        messages.success(self.request, f'Cargo {object} creado exitosamente')
        return response
    
class CargoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'core/cargo/form.html'
    permission_required = 'core.change_cargo'
    success_url = reverse_lazy('core:cargo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar cargo'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombre
        messages.success(self.request, f'Cargo {object} actualizado exitosamente')
        return response

class CargoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Cargo
    template_name = 'fragments/delete.html'
    permission_required = 'core.delete_cargo'
    success_url = reverse_lazy('core:cargo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object.nombre
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombre
        messages.success(self.request, f'Cargo {object} eliminado exitosamente')
        return response