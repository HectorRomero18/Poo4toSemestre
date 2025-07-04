from django import forms
from django.forms import ModelForm
from applications.core.models import Empleado

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombres',
            'apellidos',
            'cedula_ecuatoriana',
            'dni',
            'fecha_nacimiento',
            'cargo',
            'sueldo',
            'fecha_ingreso',
            'direccion',
            'latitud',
            'longitud',
            'foto',
            'activo',
        ]

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'cedula_ecuatoriana': 'Cédula',
            'dni': 'DNI Internacional',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'cargo': 'Cargo',
            'sueldo': 'Sueldo',
            'fecha_ingreso': 'Fecha de Ingreso',
            'direccion': 'Dirección',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'foto': 'Foto',
            'activo': 'Activo',
        }

        widgets = {
            'nombres': forms.TextInput(attrs={
                'placeholder': 'Ingrese los nombres',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'apellidos': forms.TextInput(attrs={
                'placeholder': 'Ingrese los apellidos',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'cedula_ecuatoriana': forms.TextInput(attrs={
                'placeholder': 'Ingrese la cédula (10 dígitos)',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'dni': forms.TextInput(attrs={
                'placeholder': 'Pasaporte, DNI, CURP…',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'cargo': forms.Select(attrs={
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full',
            }),
            'sueldo': forms.NumberInput(attrs={
                'placeholder': '0.00',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'fecha_ingreso': forms.DateInput(attrs={
                'type': 'date',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Dirección completa',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'latitud': forms.NumberInput(attrs={
                'placeholder': 'Latitud',
                'step': 'any',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'longitud': forms.NumberInput(attrs={
                'placeholder': 'Longitud',
                'step': 'any',
                'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            }),
        }

        error_messages = {
            'cedula_ecuatoriana': {
                'invalid': 'Cédula no válida.',
            },
            'dni': {
                'invalid': 'DNI internacional no válido.',
            },
        }

    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres", "").strip().title()
        return nombres

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos", "").strip().title()
        return apellidos

    def clean_dni(self):
        dni = self.cleaned_data.get("dni", "")
        if dni:
            dni = dni.strip().upper()
        return dni
