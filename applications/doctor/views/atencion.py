from django.shortcuts import get_object_or_404, render
from applications.doctor.models import Atencion, DetalleAtencion

def ver_detalle_atencion(request, atencion_id):
    atencion = get_object_or_404(Atencion, id=atencion_id)
    detalles = atencion.detalles.all()  # DetalleAtencion tiene related_name="detalles"
    
    return render(request, 'doctor/ver_detalle_atencion.html', {
        'atencion': atencion,
        'detalles': detalles
    })