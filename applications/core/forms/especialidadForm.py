from django import forms
from django.forms import ModelForm
from applications.core.models import Especialidad

class EspecialidadForm(ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre', 'descripcion', 'activo']

        labels = {
            'nombre': 'Nombre de la Especialidad',
            'descripcion': 'Descripción',
            'activo': 'Activo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingrese el nombre de la especialidad',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Ingrese una descripción de la especialidad',
                'rows': 3,
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            }),
        }

        error_messages = {
            'nombre': {
                'unique': 'Ya existe una especialidad con este nombre.',
            },
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip().capitalize()
        if Especialidad.objects.exclude(pk=self.instance.pk).filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Este nombre de especialidad ya está registrado.")
        return nombre
