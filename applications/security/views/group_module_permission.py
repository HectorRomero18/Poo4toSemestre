from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import Group
from applications.security.models import GroupModulePermission, Module
from applications.security.forms.group_module_permission import GroupModulePermissionForm
from applications.security.components.mixin_crud import (
    ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin, PermissionMixin
)


class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/group_module_permission/list.html'
    model = GroupModulePermission
    context_object_name = 'group_permissions'
    permission_required = 'view_groupmodulepermission'
    
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            self.query.add(Q(group__name__icontains=q), Q.OR)
            self.query.add(Q(module__name__icontains=q), Q.OR)
            self.query.add(Q(module__menu__name__icontains=q), Q.OR)
        return self.model.objects.select_related('group', 'module', 'module__menu').filter(self.query).order_by('group__name', 'module__name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:groupmodulepermission_create')
        return context


class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GroupModulePermission
    form_class = GroupModulePermissionForm
    template_name = 'security/group_module_permission/form.html'
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'add_groupmodulepermission'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Crear Permiso de Grupo'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 
            f"Éxito al crear el permiso para el grupo: {self.object.group.name} - {self.object.module.name}."
        )
        return response


class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    form_class = GroupModulePermissionForm
    template_name = 'security/group_module_permission/form.html'
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'change_groupmodulepermission'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Permiso de Grupo'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 
            f"Éxito al actualizar el permiso para el grupo: {self.object.group.name} - {self.object.module.name}."
        )
        return response


class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:groupmodulepermission_list')
    permission_required = 'delete_groupmodulepermission'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Permiso de Grupo'
        context['description'] = f"¿Desea eliminar el permiso del grupo: {self.object.group.name} para el módulo: {self.object.module.name}?"
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        group_name = self.object.group.name
        module_name = self.object.module.name
        response = super().form_valid(form)
        messages.success(
            self.request, 
            f"Éxito al eliminar el permiso del grupo: {group_name} para el módulo: {module_name}."
        )
        return response


# Vista AJAX para obtener permisos del módulo
def get_module_permissions(request):
    """
    Vista AJAX para obtener los permisos disponibles para un módulo específico
    """
    module_id = request.GET.get('module_id')
    if not module_id:
        return JsonResponse({'permissions': []})
    
    try:
        module = Module.objects.get(id=module_id)
        permissions = module.permissions.all().values('id', 'name', 'codename')
        return JsonResponse({'permissions': list(permissions)})
    except Module.DoesNotExist:
        return JsonResponse({'permissions': []})