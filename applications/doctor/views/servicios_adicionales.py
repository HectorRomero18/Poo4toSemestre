
from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.doctor.forms.servicios_adicionales import ServiciosAdicionalesForm
from applications.doctor.models import ServiciosAdicionales
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect


class ServiciosAdicionalesListView(PermissionMixin, ListView, ListViewMixin):
    model = ServiciosAdicionales
    context_object_name = 'servicios'
    permission_required = 'view_serviciosadicionales'
    template_name = 'doctor/servicios/list.html'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if not hasattr(self, 'query') or self.query is None:
            self.query = Q()
        
        if q1 is not None:
            self.query.add(Q(nombre_servicio__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:servicios_create')
        return context
    
class ServiciosAdicionalesCreateView(PermissionMixin, CreateView, CreateViewMixin):
    model = ServiciosAdicionales
    permission_required = 'add_serviciosadicionales'
    form_class = ServiciosAdicionalesForm
    template_name = 'doctor/servicios/form.html'
    success_url = reverse_lazy('doctor:servicios_list')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['grabar'] = 'Crear'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Servicio Agregado correctamente!')
        return response

    
class ServiciosAdicionalesUpdateView(PermissionMixin, UpdateView, UpdateViewMixin):
    model = ServiciosAdicionales
    permission_required = 'change_serviciosadicionales'
    form_class = ServiciosAdicionalesForm
    template_name = 'doctor/servicios/form.html'
    success_url = reverse_lazy('doctor:servicios_list')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Servicio actualizado correctamente!')
        return response
    
class ServiciosAdicionalesDeleteView(PermissionMixin, DeleteView, DeleteViewMixin):
    model = ServiciosAdicionales
    permission_required = 'change_serviciosadicionales'
    success_url = reverse_lazy('doctor:servicios_list')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['description'] = 'Estas seguro de eliminar este servicio'
        context['back_url'] = self.success_url
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"No se puede eliminar el servicio '{self.object.nombre_servicio}' porque está asociado a uno o más pagos."
            )
            return redirect(self.success_url)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Servicio eliminado correctamente!')
        return response