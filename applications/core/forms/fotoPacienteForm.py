from django import forms
from applications.core.models import FotoPaciente

class FotoPacienteForm(forms.ModelForm):
    class Meta:
        model = FotoPaciente
        fields = ['paciente', 'imagen', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
