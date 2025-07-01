from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.group_module_permission import GroupModulePermissionForm
from applications.security.models import GroupModulePermission
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    model = GroupModulePermission
    template_name = 'security/group_module_permission/list.html'
    permission_required = 'view_groupmodulepermission'
    context_object_name = 'group_module_permissions'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is not None:
            self.query.add(Q(group__name__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:group_module_permission_create')
        return context
    


class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GroupModulePermission
    form_class = GroupModulePermissionForm
    template_name = 'security/group_module_permission/form.html'
    permission_required = 'add_groupmodulepermission'
    success_url = reverse_lazy('security:group_module_permission_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Crear'
        context['back_url'] = self.success_url
        context['grouped_permissions'] = context['form'].grouped_permissions
        return context

    def form_valid(self, form):
        instance = form.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'group': instance.group.name,
                'module': instance.module.name,
                'permissions': list(instance.permissions.values_list('name', flat=True)),
            })
        messages.success(self.request, 'Group Module Permission creado exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

    
class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    permission_required = 'change_groupmodulepermission'
    form_class = GroupModulePermissionForm
    template_name = 'security/group_module_permission/form.html'
    success_url = reverse_lazy('security:group_module_permission_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Group Module Permission actualizado exitosamente')
        return response
    
class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    permission_required = 'delete_groupmodulepermission'
    success_url = reverse_lazy('security:group_module_permission_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar'
        context['back_url'] = self.success_url
        context['description'] = '¿Desea eliminar el Group Module Permission?'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Group Module Permission eliminado exitosamente')
        return response

