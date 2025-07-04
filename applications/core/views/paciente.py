from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from applications.core.models import Paciente
from django.contrib import messages
from applications.core.forms.pacienteForm import PacienteForm
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect

"""  Vista para buscar pacientes mediante AJAX. Por nombres, apellidos, cédula o teléfono. """


@login_required
@require_http_methods(["GET"])
def paciente_find(request):
    try:
        # Obtener el parámetro de búsqueda
        query = request.GET.get('q', '').strip()

        # Validar que se proporcione al menos 3 caracteres
        if len(query) < 3:
            return JsonResponse({
                'success': False,
                'message': 'Debe proporcionar al menos 3 caracteres para la búsqueda',
                'pacientes': []
            })

        # Construir la consulta de búsqueda
        # Buscar en nombres, apellidos, cédula, DNI y teléfono
        pacientes_query = Paciente.objects.filter(
            Q(activo=True) & (
                    Q(nombres__icontains=query) |
                    Q(apellidos__icontains=query) |
                    Q(cedula_ecuatoriana__icontains=query) |
                    Q(dni__icontains=query) |
                    Q(telefono__icontains=query)
            )
        ).select_related('tipo_sangre').prefetch_related(
            'atenciones__diagnostico',
            'atenciones__detalles__medicamento'
        ).order_by('apellidos', 'nombres')

        # Limitar resultados para mejorar rendimiento
        pacientes_query = pacientes_query[:20]

        # Convertir a lista de diccionarios
        pacientes_data = []
        for paciente in pacientes_query:
            # Calcular edad
            edad = paciente.edad

            # Obtener atenciones anteriores (últimas 10)
            atenciones = []
            for atencion in paciente.atenciones.all()[:10]:
                # Obtener prescripciones/detalles de esta atención
                detalles = []
                for detalle in atencion.detalles.all():
                    detalle_dict = {
                        'medicamento': detalle.medicamento.nombre if detalle.medicamento else None,
                        'cantidad': detalle.cantidad,
                        'prescripcion': detalle.prescripcion,
                        'duracion_tratamiento': detalle.duracion_tratamiento,
                        'frecuencia_diaria': detalle.frecuencia_diaria,
                    }
                    detalles.append(detalle_dict)

                # Obtener diagnósticos
                diagnosticos = [d.descripcion for d in atencion.diagnostico.all()]

                # Determinar tipo de consulta
                tipo_consulta = "Chequeo"
                if atencion.es_control:
                    tipo_consulta = "Control"
                elif "urgencia" in atencion.motivo_consulta.lower() or "dolor" in atencion.motivo_consulta.lower():
                    tipo_consulta = "Urgencia"

                atencion_dict = {
                    'id': atencion.id,
                    'fecha_atencion': atencion.fecha_atencion.isoformat(),
                    'tipo_consulta': tipo_consulta,

                    # Signos vitales
                    'presion_arterial': atencion.presion_arterial,
                    'pulso': atencion.pulso,
                    'temperatura': float(atencion.temperatura) if atencion.temperatura else None,
                    'frecuencia_respiratoria': atencion.frecuencia_respiratoria,
                    'saturacion_oxigeno': float(atencion.saturacion_oxigeno) if atencion.saturacion_oxigeno else None,
                    'peso': float(atencion.peso) if atencion.peso else None,
                    'altura': float(atencion.altura) if atencion.altura else None,
                    'imc': atencion.calcular_imc,

                    # Contenido de la atención
                    'motivo_consulta': atencion.motivo_consulta,
                    'sintomas': atencion.sintomas,
                    'tratamiento': atencion.tratamiento,
                    'diagnosticos': diagnosticos,
                    'examen_fisico': atencion.examen_fisico,
                    'examenes_enviados': atencion.examenes_enviados,
                    'comentario_adicional': atencion.comentario_adicional,
                    'es_control': atencion.es_control,

                    # Prescripciones
                    'prescripciones': detalles
                }
                atenciones.append(atencion_dict)

            paciente_dict = {
                'id': paciente.id,
                'nombres': paciente.nombres,
                'apellidos': paciente.apellidos,
                'cedula_ecuatoriana': paciente.cedula_ecuatoriana,
                'dni': paciente.dni,
                'fecha_nacimiento': paciente.fecha_nacimiento.isoformat() if paciente.fecha_nacimiento else None,
                'edad': edad,
                'telefono': paciente.telefono,
                'email': paciente.email,
                'sexo': paciente.sexo,
                'estado_civil': paciente.estado_civil,
                'direccion': paciente.direccion,
                'latitud': float(paciente.latitud) if paciente.latitud else None,
                'longitud': float(paciente.longitud) if paciente.longitud else None,
                'tipo_sangre': paciente.tipo_sangre.tipo if paciente.tipo_sangre else None,
                'foto_url': paciente.get_image,

                # Historia clínica
                'antecedentes_personales': paciente.antecedentes_personales,
                'antecedentes_quirurgicos': paciente.antecedentes_quirurgicos,
                'antecedentes_familiares': paciente.antecedentes_familiares,
                'alergias': paciente.alergias,
                'medicamentos_actuales': paciente.medicamentos_actuales,
                'habitos_toxicos': paciente.habitos_toxicos,
                'vacunas': paciente.vacunas,
                'antecedentes_gineco_obstetricos': paciente.antecedentes_gineco_obstetricos,

                # Atenciones anteriores
                'atenciones': atenciones,
                'total_atenciones': paciente.atenciones.count()
            }
            pacientes_data.append(paciente_dict)
        print(pacientes_data)
        return JsonResponse({
            'success': True,
            'pacientes': pacientes_data,
            'total': len(pacientes_data),
            'query': query
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error en la búsqueda: {str(e)}',
            'pacientes': []
        }, status=500)



class PacienteListView(PermissionMixin, ListView, ListViewMixin):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'core/pacientes/list.html'
    permission_required = 'view_paciente'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if not hasattr(self, 'query') or self.query is None:
            self.query = Q()
        if q1 is not None:
            self.query.add(Q(nombres__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:paciente_create')
        return context

class PacienteCreateView(PermissionMixin, CreateView, CreateViewMixin):
    model = Paciente
    form_class = PacienteForm
    permission_required = 'add_paciente'
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('core:pacientes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Crear Paciente'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Paciente creado exitosamente')
        return response
    
class PacienteUpdateView(PermissionMixin, UpdateView, UpdateViewMixin):
    model = Paciente
    form_class = PacienteForm
    permission_required = 'change_paciente'
    template_name = 'core/pacientes/form.html'
    success_url = reverse_lazy('core:pacientes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualzar Paciente'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Paciente actualizado exitosamente')
        return response
class PacienteDeleteView(PermissionMixin, DeleteView, DeleteViewMixin):
    model = Paciente
    permission_required = 'delete_paciente'
    success_url = reverse_lazy('core:pacientes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description'] = 'Estas seguro de eliminar el Paciente?'
        context['back_url'] = self.success_url
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request,
                f"No se puede eliminar el servicio '{self.object.nombre_completo}' porque está asociado a uno o más atenciones."
            )
            return redirect(self.success_url)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Paciente eliminado exitosamente')
        return response
    