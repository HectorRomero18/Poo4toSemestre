from django import forms
from django.forms import ModelForm
from applications.core.models import TipoSangre

class TipoSangreForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ['tipo', 'descripcion']

        labels = {
            'tipo': 'Tipo de Sangre',
            'descripcion': 'Descripción',
        }

        widgets = {
            'tipo': forms.TextInput(attrs={
                'placeholder': 'Ingrese el tipo de sangre (ej. A+, O-, B+)',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Ingrese una descripción del tipo de sangre',
                'rows': 3,
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full',
            }),
        }

        error_messages = {
            'tipo': {
                'unique': 'Este tipo de sangre ya está registrado.',
            },
        }

    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo", "").strip().upper()
        if TipoSangre.objects.exclude(pk=self.instance.pk).filter(tipo__iexact=tipo).exists():
            raise forms.ValidationError("Este tipo de sangre ya está registrado.")
        return tipo
