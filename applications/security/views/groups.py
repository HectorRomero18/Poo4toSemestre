
from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.menu import MenuForm
from applications.security.forms.module import ModuleForm
from applications.security.forms.groups import GroupForm
from applications.security.models import Menu, Module, Group
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


class GroupsListView(PermissionMixin, ListViewMixin, ListView):
    model = Group
    template_name = 'security/groups/list.html'
    context_object_name = 'groups'
    permission_required = 'view_group'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q is not None:
            self.query.add(Q(name__icontains=q), Q.OR)
            
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:groups_create')
        return context
    
class GroupsCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'security/groups/form.html'
    permission_required = 'add_group'
    success_url = reverse_lazy('security:group_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Crear'
        context['back_url'] = self.success_url
        return context
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.name
        messages.success(self.request, f'Grupo {object} creado correctamente')
        return response
    
class GroupsUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'security/groups/form.html'
    permission_required = 'change_group'
    success_url = reverse_lazy('security:group_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.name
        messages.success(self.request, f'Grupo {object} actualizado correctamente')
        return response
    
class GroupsDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Group
    template_name = 'security/groups/delete.html'
    permission_required = 'delete_group'
    success_url = reverse_lazy('security:group_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        context['decription'] = '¿ Estas seguro de eliminar este grupo ? '

        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.name
        messages.success(self.request, f'Grupo {object} eliminado correctamente')
        return response
        