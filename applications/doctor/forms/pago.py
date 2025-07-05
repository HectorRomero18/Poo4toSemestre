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
            'pago': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'servicio_adicional': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descuento_porcentaje': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0, 'max': 100}),
            'aplica_seguro': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'valor_seguro': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descripcion_seguro': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        pago_instance = kwargs.pop('pago_instance', None)
        super().__init__(*args, **kwargs)

        # 🔒 Desactiva validación en campo deshabilitado
        self.fields['pago'].required = False
        self.fields['pago'].disabled = True

        # Campo oculto que sí se envía
        self.fields['pago_hidden'] = forms.ModelChoiceField(
            queryset=self.fields['pago'].queryset,
            widget=forms.HiddenInput(),
            required=True
        )

        if pago_instance:
            self.fields['pago'].initial = pago_instance
            self.fields['pago_hidden'].initial = pago_instance
        elif self.instance and self.instance.pago_id:
            self.fields['pago'].initial = self.instance.pago_id
            self.fields['pago_hidden'].initial = self.instance.pago_id
