from django import forms
from applications.core.models import TipoMedicamento

class TipoMedicamentoForm(forms.ModelForm):
    class Meta:
        model = TipoMedicamento
        fields = ['nombre', 'descripcion', 'activo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
