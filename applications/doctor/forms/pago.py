from django import forms
from applications.doctor.models import Pago, DetallePago
from django.forms.models import inlineformset_factory

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'atencion',
            'metodo_pago',
            'monto_total',
            'estado',
            'nombre_pagador',
            'fecha_pago',
            'referencia_externa',
            'evidencia_pago',
            'observaciones',
            'activo',
        ]

class DetallePagoForm(forms.ModelForm):
    class Meta:
        model = DetallePago
        fields = [
            'pago',
            'servicio_adicional',
            'cantidad',
            'precio_unitario',
            'descuento_porcentaje',
            'aplica_seguro',
            'valor_seguro',
            'descripcion_seguro',
        ]
        widgets = {
            'pago': forms.Select(attrs={'class': 'form-control'}),
            'servicio_adicional': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descuento_porcentaje': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0, 'max': 100}),
            'aplica_seguro': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'valor_seguro': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descripcion_seguro': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Campo oculto o manejado internamente si se desea (por ejemplo, si el pago ya está creado)
        # self.fields['pago'].widget = forms.HiddenInput()

        # Puedes agregar validaciones o configuraciones condicionales aquí si lo necesitas.
