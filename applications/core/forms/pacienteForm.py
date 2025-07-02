from django import forms
from applications.core.models import Paciente
class PacienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
        }),
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
            'nombres': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Ingrese los nombres'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Ingrese los apellidos'
            }),
            'cedula_ecuatoriana': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': '1234567890'
            }),
            'dni': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Pasaporte, DNI, CURP, etc.'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': '+593 999 123 456'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'ejemplo@correo.com'
            }),
            'sexo': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'estado_civil': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'tipo_sangre': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Ingrese la dirección completa'
            }),
            'latitud': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Ej: -2.170998'
            }),
            'longitud': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'Ej: -79.922359'
            }),
            'antecedentes_personales': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Ej.: Diabetes tipo 2, hipertensión, asma, etc.'
            }),
            'antecedentes_quirurgicos': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Ej.: Cirugías previas como apendicectomía, cesárea, etc.'
            }),
            'antecedentes_familiares': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Enfermedades hereditarias (padres, abuelos, hermanos).'
            }),
            'alergias': forms.Textarea(attrs={
                'rows': 2,
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Ej.: Penicilina, mariscos, polvo, etc.'
            }),
            'medicamentos_actuales': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Nombre, dosis y frecuencia. Ej.: Losartán 50mg diario.'
            }),
            'habitos_toxicos': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Ej.: Tabaco, alcohol, drogas, sedentarismo, etc.'
            }),
            'vacunas': forms.Textarea(attrs={
                'rows': 2,
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Vacunas importantes recibidas. Ej.: COVID-19, influenza, etc.'
            }),
            'antecedentes_gineco_obstetricos': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent',
                'placeholder': 'Solo en mujeres. Ej.: menarquia, embarazos, anticonceptivos.'
            }),
        }