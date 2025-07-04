from django import forms
from applications.doctor.models import ServiciosAdicionales

class ServiciosAdicionalesForm(forms.ModelForm):
    class Meta:
        model = ServiciosAdicionales
        fields = ['nombre_servicio', 'costo_servicio', 'descripcion', 'activo']
        widgets = {
            'nombre_servicio': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ejemplo: Radiografía, Laboratorio clínico'
            }),
            'costo_servicio': forms.NumberInput(attrs={
                'class': 'form-input',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Ejemplo: 25.00'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 3,
                'placeholder': 'Descripción opcional del servicio'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }
        labels = {
            'nombre_servicio': 'Nombre del Servicio',
            'costo_servicio': 'Costo del Servicio (USD)',
            'descripcion': 'Descripción del Servicio',
            'activo': 'Activo',
        }
        help_texts = {
            'nombre_servicio': 'Ejemplo: Radiografía, Laboratorio clínico, Procedimiento menor.',
            'costo_servicio': 'Costo unitario del servicio en dólares. Ejemplo: 25.00',
            'descripcion': 'Descripción opcional del servicio. Ejemplo: Examen de sangre de rutina.',
            'activo': 'Marca si el servicio adicional está disponible para agendar o prescribir.',
        }
