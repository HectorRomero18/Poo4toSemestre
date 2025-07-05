from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .faqs import FAQS
import unicodedata
import re
import difflib

def index(request):
    return render(request, 'chatbot/index.html')

def limpiar_texto(texto):
    """
    Convierte el texto a minúsculas, quita tildes y signos de puntuación.
    """
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto.strip()

def buscar_respuesta(mensaje, faqs):
    mensaje = mensaje.lower().strip()

    # Intentar coincidencia exacta
    if mensaje in faqs:
        return faqs[mensaje]

    # Buscar la clave más parecida
    posibles = difflib.get_close_matches(mensaje, faqs.keys(), n=1, cutoff=0.5)
    if posibles:
        return faqs[posibles[0]]

    # Si no encuentra nada razonable
    return 'No encontré una respuesta para tu pregunta.'

@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            mensaje = data.get('mensaje', '').lower().strip()

            respuesta = buscar_respuesta(mensaje, FAQS)

            return JsonResponse({'respuesta': respuesta})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
