from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.core.forms.doctorForm import DoctorForm
from applications.core.models import Doctor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class DoctorListView(PermissionMixin, ListViewMixin, ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    permission_required = 'core.view_doctor'
    context_object_name = 'doctors'

    def get_queryset(self):
        q = self.request.GET.get('q')

        if q is not None:
            self.query.add(Q(nombre__icontains=q), Q.OR)
            self.query.add(Q(apellido__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:doctor_create')
        return context
    
class DoctorCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    permission_required = 'core.add_doctor'
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Crear doctor'
        context['back_url'] = self.success_url
        context['cancelar'] = 'Cancelar'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombre
        messages.success(self.request, f'Doctor {object} creado exitosamente')
        return response

class DoctorUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    permission_required = 'core.change_doctor'
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar doctor'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.nombre
        messages.success(self.request, f'Doctor {object} actualizado exitosamente')
        return response
    
class DoctorDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Doctor
    template_name = 'core/doctor/delete.html'
    permission_required = 'core.delete_doctor'
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object.nombre
        return context
    
    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        messages.success(request, f'Doctor {object.nombre} eliminado exitosamente')
        return super().delete(request, *args, **kwargs)