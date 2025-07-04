from django import forms
from django.forms import ModelForm
from applications.core.models import Cargo

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre', 'descripcion', 'activo']

        labels = {
            'nombre': 'Nombre del Cargo',
            'descripcion': 'Descripción',
            'activo': 'Activo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej.: Médico, Enfermero, Administrador',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Breve descripción del cargo (opcional)',
                'rows': 3,
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            }),
        }

        error_messages = {
            'nombre': {
                'unique': 'Ya existe un cargo con este nombre.',
            },
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip().capitalize()
        if Cargo.objects.exclude(pk=self.instance.pk).filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Este nombre de cargo ya está registrado.")
        return nombre
