from django import forms
from django.contrib.auth.models import Group, Permission
from applications.security.models import GroupModulePermission, Module


class GroupModulePermissionForm(forms.ModelForm):
    class Meta:
        model = GroupModulePermission
        fields = ['group', 'module', 'permissions']
        widgets = {
            'group': forms.Select(attrs={
                'class': 'field-select',
                'id': 'id_group'
            }),
            'module': forms.Select(attrs={
                'class': 'field-select',
                'id': 'id_module'
            }),
            'permissions': forms.CheckboxSelectMultiple(attrs={
                'class': 'permissions-checkbox',
                'id': 'id_permissions'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Configurar queryset para grupos
        self.fields['group'].queryset = Group.objects.all().order_by('name')
        self.fields['group'].empty_label = "Seleccione un grupo"

        # Configurar queryset para módulos activos
        self.fields['module'].queryset = Module.objects.filter(is_active=True).select_related('menu').order_by('menu__name', 'name')
        self.fields['module'].empty_label = "Seleccione un módulo"

        if self.instance and self.instance.pk:
            # Modo edición: mostrar permisos del módulo ya asociados
            if self.instance.module:
                self.fields['permissions'].queryset = self.instance.module.permissions.all()
            else:
                self.fields['permissions'].queryset = Permission.objects.none()
        else:
            # Modo creación: cargar permisos según módulo enviado vía POST
            if 'module' in self.data:
                try:
                    module_id = int(self.data.get('module'))
                    module = Module.objects.get(id=module_id)
                    self.fields['permissions'].queryset = module.permissions.all()
                except (ValueError, Module.DoesNotExist):
                    self.fields['permissions'].queryset = Permission.objects.none()
            else:
                self.fields['permissions'].queryset = Permission.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        group = cleaned_data.get('group')
        module = cleaned_data.get('module')

        # Validar que no exista ya la combinación grupo-módulo
        if group and module:
            existing = GroupModulePermission.objects.filter(
                group=group,
                module=module
            ).exclude(pk=self.instance.pk if self.instance else None)

            if existing.exists():
                raise forms.ValidationError(
                    f"Ya existe un permiso para el grupo '{group.name}' y el módulo '{module.name}'"
                )

        return cleaned_data
