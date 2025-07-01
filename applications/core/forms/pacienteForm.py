from django import forms
from applications.core.models import Paciente

class PacienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de Nacimiento"
    )
    foto = forms.ImageField(
        required=False,
        label="Foto del Paciente"
    )

    class Meta:
        model = Paciente
        fields = [
            'nombres',
            'apellidos',
            'cedula_ecuatoriana',
            'dni',
            'fecha_nacimiento',
            'telefono',
            'email',
            'sexo',
            'estado_civil',
            'direccion',
            'latitud',
            'longitud',
            'tipo_sangre',
            'foto',
            'antecedentes_personales',
            'antecedentes_quirurgicos',
            'antecedentes_familiares',
            'alergias',
            'medicamentos_actuales',
            'habitos_toxicos',
            'vacunas',
            'antecedentes_gineco_obstetricos',
        ]
        widgets = {
            'sexo': forms.Select(),
            'estado_civil': forms.Select(),
            'tipo_sangre': forms.Select(),
            'antecedentes_personales': forms.Textarea(attrs={'rows': 3}),
            'antecedentes_quirurgicos': forms.Textarea(attrs={'rows': 3}),
            'antecedentes_familiares': forms.Textarea(attrs={'rows': 3}),
            'alergias': forms.Textarea(attrs={'rows': 2}),
            'medicamentos_actuales': forms.Textarea(attrs={'rows': 3}),
            'vacunas': forms.Textarea(attrs={'rows': 2}),
            'antecedentes_gineco_obstetricos': forms.Textarea(attrs={'rows': 3}),
        }