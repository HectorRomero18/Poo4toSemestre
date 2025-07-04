from django import forms
from applications.doctor.models import CitaMedica

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'hora_cita': forms.TimeInput(attrs={'type': 'time', 'class': 'form-input'}),
        }