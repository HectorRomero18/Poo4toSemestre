from django import forms
from applications.doctor.models import CitaMedica

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['paciente', 'doctor', 'fecha', 'hora_cita', 'estado', 'observaciones']
