from django import forms
from django.forms import ModelForm
from applications.core.models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "nombres", "apellidos", "ruc", "fecha_nacimiento", "direccion",
            "latitud", "longitud", "codigo_unico_doctor", "especialidad",
            "telefonos", "email", "horario_atencion", "duracion_atencion",
            "curriculum", "firma_digital", "foto", "imagen_receta", "activo"
        ]

        labels = {
            "nombres": "Nombres",
            "apellidos": "Apellidos",
            "ruc": "RUC",
            "fecha_nacimiento": "Fecha de Nacimiento",
            "direccion": "Dirección de Trabajo",
            "latitud": "Latitud",
            "longitud": "Longitud",
            "codigo_unico_doctor": "Código Único",
            "especialidad": "Especialidades",
            "telefonos": "Teléfonos",
            "email": "Correo Electrónico",
            "horario_atencion": "Horario de Atención",
            "duracion_atencion": "Duración de Cita",
            "curriculum": "Currículum Vitae",
            "firma_digital": "Firma Digital",
            "foto": "Foto",
            "imagen_receta": "Imagen para Recetas",
            "activo": "Activo",
        }

        widgets = {
            "nombres": forms.TextInput(attrs={
                "placeholder": "Ingrese nombres",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "apellidos": forms.TextInput(attrs={
                "placeholder": "Ingrese apellidos",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "ruc": forms.TextInput(attrs={
                "placeholder": "Ingrese RUC válido",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "fecha_nacimiento": forms.DateInput(attrs={
                "type": "date",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "direccion": forms.TextInput(attrs={
                "placeholder": "Ingrese dirección",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "latitud": forms.NumberInput(attrs={
                "placeholder": "Latitud GPS",
                "step": "0.000001",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "longitud": forms.NumberInput(attrs={
                "placeholder": "Longitud GPS",
                "step": "0.000001",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "codigo_unico_doctor": forms.TextInput(attrs={
                "placeholder": "Ingrese código único",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "especialidad": forms.SelectMultiple(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full",
            }),
            "telefonos": forms.TextInput(attrs={
                "placeholder": "Ingrese teléfonos",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Correo electrónico (opcional)",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "horario_atencion": forms.Textarea(attrs={
                "placeholder": "Ejemplo: Lunes a Viernes, 08h00 - 13h00",
                "rows": 3,
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full",
            }),
            "duracion_atencion": forms.NumberInput(attrs={
                "placeholder": "Duración en minutos",
                "min": "1",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
            }),
        }

    def clean_ruc(self):
        ruc = self.cleaned_data.get("ruc")
        if Doctor.objects.exclude(pk=self.instance.pk).filter(ruc=ruc).exists():
            raise forms.ValidationError("Este RUC ya está registrado para otro doctor.")
        return ruc

    def clean_codigo_unico_doctor(self):
        codigo = self.cleaned_data.get("codigo_unico_doctor")
        if Doctor.objects.exclude(pk=self.instance.pk).filter(codigo_unico_doctor=codigo).exists():
            raise forms.ValidationError("Este código único ya está asignado a otro doctor.")
        return codigo
