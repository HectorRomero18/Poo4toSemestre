from django import forms
from applications.doctor.models import HorarioAtencion

class HorarioAtencionForm(forms.ModelForm):
    class Meta:
        model = HorarioAtencion
        fields = '__all__'
        widgets = {
            'dia_semana': forms.Select(attrs={'class': 'form-select'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'intervalo_desde': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'intervalo_hasta': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }