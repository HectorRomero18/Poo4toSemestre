from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from applications.doctor.models import DetalleAtencion

def receta_imprimir(request, detalle_id):
    detalle = get_object_or_404(DetalleAtencion, pk=detalle_id)
    return render(request, 'doctor/receta_pdf.html', {'detalle': detalle})


