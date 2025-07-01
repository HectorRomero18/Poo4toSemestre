import re
from django import forms
from django.forms import ModelForm
from applications.security.models import Group  # Usa tu modelo personalizado si existe

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]  # Agrega aquí otros campos si tu modelo los tiene
        labels = {
            "name": "Nombre del Grupo",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre del grupo",
                "id": "id_name",
                "class": (
                    "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg "
                    "focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 "
                    "dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 "
                    "dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
                ),
            }),
        }
        error_messages = {
            "name": {
                "unique": "Ya existe un grupo con este nombre.",
                "required": "El nombre del grupo es obligatorio.",
                "max_length": "El nombre del grupo es demasiado largo.",
            },
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        if not name:
            raise forms.ValidationError("El nombre del grupo es obligatorio.")
        name = name.strip().capitalize()
        if len(name) < 3:
            raise forms.ValidationError("El nombre del grupo debe tener al menos 3 caracteres.")
        return name