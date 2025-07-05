from django.conf import settings
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed
from django.contrib.sites.shortcuts import get_current_site

@csrf_exempt
def pago_paypal(request, monto, atencion_id):
    base_url = f"https://{get_current_site(request).domain}"  # ✔️ solo esto

    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    invoice_id = f"atencion-{atencion_id}"

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": f"{monto:.2f}",
        "item_name": "Pago de Atención médica",
        "invoice": invoice_id,
        "currency_code": "USD",
        "notify_url": f"{base_url}{reverse('paypal-ipn')}",
        "return_url": f"{base_url}/doctor/pago-exitoso/",
        "cancel_return": f"{base_url}/doctor/pago-cancelado/",
        "custom": str(atencion_id),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "doctor/pago/paypal_form.html", {"form": form})

def pago_exitoso(request):
    return render(request, 'doctor/pago/pago_exitoso.html')

def pago_cancelado(request):
    return render(request, 'doctor/pago/pago_cancelado.html')

