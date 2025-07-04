from django import forms
from django.forms import ModelForm
from applications.core.models import TipoSangre

class TipoSangreForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ['tipo',
                  'descripcion']
        widgets = {
            'tipo': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Ingrese el tipo de sangre (ej. A+, O-, B+)',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Ingrese una descripción del tipo de sangre',
                'rows': 3
            }),
        }