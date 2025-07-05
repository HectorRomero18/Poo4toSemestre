from django import forms
from applications.core.models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            'nombre', 'tipo', 'marca_medicamento', 'descripcion',
            'concentracion', 'via_administracion', 'cantidad',
            'precio', 'comercial', 'foto', 'activo'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
