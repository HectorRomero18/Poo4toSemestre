from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from applications.doctor.models import Pago, Atencion

@receiver(valid_ipn_received)
def crear_pago(sender, **kwargs):
    ipn = sender

    if ipn.payment_status == ST_PP_COMPLETED:
        atencion_id = ipn.custom
        monto = ipn.mc_gross
        metodo = 'paypal'
        nombre_pagador = ipn.payer_email
        referencia = ipn.txn_id

        try:
            atencion = Atencion.objects.get(id=atencion_id)
        except Atencion.DoesNotExist:
            atencion = None

        # Evitar pagos duplicados por mismo txn_id
        if not Pago.objects.filter(referencia_externa=referencia).exists():
            Pago.objects.create(
                nombre_pagador=nombre_pagador,
                monto_total=monto,
                metodo_pago=metodo,
                referencia_externa=referencia,
                observaciones='Pago confirmado por PayPal',
                evidencia_pago=f"Pagado vía PayPal txn_id: {referencia}",
                estado='pagado',
                atencion=atencion
            )
