from django import forms
from django.contrib.auth.models import Group, Permission
from applications.security.models import GroupModulePermission, Module

class GroupModulePermissionForm(forms.ModelForm):
    class Meta:
        model = GroupModulePermission
        fields = ['group', 'module', 'permissions']

    @property
    def grouped_permissions(self):
        grouped = {}
        for perm in self.fields['permissions'].queryset:
            app_label = perm.content_type.app_label
            grouped.setdefault(app_label, []).append(perm)
        return grouped
