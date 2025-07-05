from django import forms
from applications.doctor.models import DetalleAtencion

class DetalleAtencionForm(forms.ModelForm):
    class Meta:
        model = DetalleAtencion
        fields = ['atencion', 'medicamento', 'cantidad', 'prescripcion', 'duracion_tratamiento', 'frecuencia_diaria']
