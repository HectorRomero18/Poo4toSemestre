
from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.user import UserForm
from applications.security.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class UserListView(PermissionMixin, ListViewMixin, ListView):
    model = User
    template_name = 'security/users/list.html'
    permission_required = 'security.view_user'
    context_object_name = 'users'

    def get_queryset(self):
        q = self.request.GET.get('q')

        if q is not None:
            self.query.add(Q(username__icontains=q), Q.OR)
            self.query.add(Q(dni__icontains=q), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:users_create')
        return context

class UserCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'security/users/form.html'
    permission_required = 'security.add_user'
    success_url = reverse_lazy('security:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Crear usuario'
        context['back_url'] = self.success_url
        context['cancelar'] = 'Cancelar'
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.username
        messages.success(self.request, f'Usuario {object} creado exitosamente')
        return response
    
class UserUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'security/users/form.html'
    permission_required = 'change_user'
    success_url = reverse_lazy('security:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar usuario'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.username
        messages.success(self.request, f'Usuario {object} actualizado exitosamente')
        return response
    
class UserDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = User
    template_name = 'security/users/delete.html'
    permission_required = 'delete_user'
    success_url = reverse_lazy('security:user_list')

    def get_context_data(self, request, *args, **kwargs):
        context = super().get(request, *args, **kwargs)
        context['grabar'] = 'Eliminar usuario'
        context['back_url'] = self.success_url
        context['description'] = '¿Estás seguro de eliminar este usuario?'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        object = self.object.username
        messages.success(self.request, f'Usuario {object} eliminado exitosamente')
        return response