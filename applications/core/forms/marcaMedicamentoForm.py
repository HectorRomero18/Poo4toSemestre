from django import forms
from applications.core.models import MarcaMedicamento

class MarcaMedicamentoForm(forms.ModelForm):
    class Meta:
        model = MarcaMedicamento
        fields = ['nombre', 'descripcion', 'activo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
