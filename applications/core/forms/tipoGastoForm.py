from django import forms
from applications.core.models import TipoGasto

class TipoGastoForm(forms.ModelForm):
    class Meta:
        model = TipoGasto
        fields = ['nombre', 'descripcion', 'activo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
