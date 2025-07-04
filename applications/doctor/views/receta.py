from django.shortcuts import get_object_or_404, render
from applications.doctor.models import DetalleAtencion, Atencion
from django.contrib.auth.decorators import login_required
from django.http import Http404

@login_required
def receta_imprimir(request, detalle_id=None, atencion_id=None):
    """
    Vista para imprimir recetas médicas.
    Puede recibir:
    - detalle_id: para imprimir un solo medicamento
    - atencion_id: para imprimir todos los medicamentos de una atención
    """
    context = {
        'titulo': 'Receta Médica',
        'fecha_actual': True
    }
    
    if detalle_id:
        # Caso 1: Imprimir una receta para un medicamento específico
        detalle = get_object_or_404(DetalleAtencion, pk=detalle_id)
        context['detalle'] = detalle
        context['atencion'] = detalle.atencion
        context['detalles'] = [detalle]  # Lista con un solo elemento
        context['modo'] = 'detalle_individual'
        
    elif atencion_id:
        # Caso 2: Imprimir todos los medicamentos de una atención
        atencion = get_object_or_404(Atencion, pk=atencion_id)
        detalles = atencion.detalles.all()
        
        if not detalles.exists():
            raise Http404("No hay medicamentos registrados para esta atención")
            
        context['atencion'] = atencion
        context['detalles'] = detalles
        context['modo'] = 'atencion_completa'
        
    else:
        raise Http404("Debe especificar un detalle_id o atencion_id")
    
    # Obtener información del doctor si está disponible
    if hasattr(context['atencion'], 'doctor') and context['atencion'].doctor:
        context['doctor'] = context['atencion'].doctor
    
    return render(request, 'doctor/receta_imprimir.html', context)