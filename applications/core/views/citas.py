from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
from applications.core.models import Paciente
from applications.doctor.models import CitaMedica, HorarioAtencion

def citas_json(request):
    anio = int(request.GET.get('anio', datetime.now().year))
    mes = int(request.GET.get('mes', datetime.now().month))
    citas = CitaMedica.objects.filter(fecha__year=anio, fecha__month=mes)
    data = [{
        "id": cita.id,
        "title": f"{cita.paciente.nombre}",
        "start": cita.fecha.isoformat()
    } for cita in citas]
    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_cita(request):
    data = json.loads(request.body)
    cedula = data['cedula']
    nombre = data['nombre']
    telefono = data.get('telefono', '')
    fecha = datetime.fromisoformat(data['fecha'])
    doctor_id = data['doctor_id']

    paciente, _ = Paciente.objects.get_or_create(
        cedula=cedula, defaults={'nombre': nombre, 'telefono': telefono}
    )

    if CitaMedica.objects.filter(doctor_id=doctor_id, fecha=fecha).exists():
        return JsonResponse({'error': 'El horario ya está ocupado'}, status=400)

    CitaMedica.objects.create(paciente=paciente, doctor_id=doctor_id, fecha=fecha)
    return JsonResponse({'mensaje': 'Cita creada'})

@csrf_exempt
def mover_cita(request, id):
    data = json.loads(request.body)
    nueva_fecha = datetime.fromisoformat(data['nueva_fecha'])
    cita = get_object_or_404(CitaMedica, pk=id)

    if CitaMedica.objects.filter(doctor=cita.doctor, fecha=nueva_fecha).exclude(pk=id).exists():
        return JsonResponse({'error': 'Horario ya ocupado'}, status=400)

    cita.fecha = nueva_fecha
    cita.save()
    return JsonResponse({'mensaje': 'Cita actualizada'})

def verificar_paciente(request):
    cedula = request.GET.get('cedula')
    existe = Paciente.objects.filter(cedula=cedula).exists()
    return JsonResponse({'existe': existe})

def verificar_disponibilidad(request):
    doctor_id = request.GET.get('doctor_id')
    fecha = request.GET.get('fecha')  # formato: 2025-07-04T14:00
    fecha_dt = datetime.fromisoformat(fecha)
    dia_semana = fecha_dt.weekday()
    hora = fecha_dt.time()

    horarios = HorarioAtencion.objects.filter(doctor_id=doctor_id, dia_semana=dia_semana)
    disponible = any(h.hora_inicio <= hora <= h.hora_fin for h in horarios)

    ocupado = CitaMedica.objects.filter(doctor_id=doctor_id, fecha=fecha_dt).exists()

    return JsonResponse({'disponible': disponible and not ocupado})
