from django.urls import path
from applications.core.views.paciente import paciente_find, PacienteCreateView,PacienteDeleteView, PacienteUpdateView, PacienteListView
from applications.core.views.diagnostico import DiagnosticoCreateView, DiagnosticoListView, DiagnosticoDeleteView, DiagnosticoUpdateView

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
     path('paciente_find/', paciente_find, name="paciente_find"),

    path('pacientes_list/', PacienteListView.as_view(), name="pacientes_list"),
    path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    path('paciente_update/<int:pk>/', PacienteUpdateView.as_view(), name="paciente_update"),
    path('paciente_delete/<int:pk>/', PacienteDeleteView.as_view(), name="paciente_delete"),
    # ... otras rutas ...
    # Rutas  para vistas relacionadas con Diagnostico
    path('diagnosticos/', DiagnosticoListView.as_view(), name='diagnostico_list'),
    path('diagnosticos/nuevo/', DiagnosticoCreateView.as_view(), name='diagnostico_create'),
    path('diagnosticos/<int:pk>/editar/', DiagnosticoUpdateView.as_view(), name='diagnostico_edit'),
    path('diagnosticos/<int:pk>/eliminar/', DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),
    # Calendario
    path('calendario/', vista_calendario, name='calendario'),

    # APIs citas
    path('api/citas/', citas_json, name='citas_json'),
    path('api/cita/nueva/', crear_cita, name='crear_cita'),
    path('api/cita/<int:id>/mover/', mover_cita, name='mover_cita'),
    path('api/paciente/existe/', verificar_paciente, name='verificar_paciente'),
    path('api/disponible/', verificar_disponibilidad, name='verificar_disponibilidad'),

    



     path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    
    # 🩸 Tipo de Sangre
    path('tiposangre_list/', TipoSangreListView.as_view(), name='tipoSangre_list'),
    path('tiposangre_create/', TipoSangreCreateView.as_view(), name='tipoSangre_create'),
    path('tiposangre_update/<int:pk>/editar/', TipoSangreUpdateView.as_view(), name='tipoSangre_update'),
    path('tiposangre_delete/<int:pk>/eliminar/', TipoSangreDeleteView.as_view(), name='tipoSangre_delete'),
    
    # 🩺 Especialidades
    path('especialidades/', EspecialidadListView.as_view(), name='especialidad_list'),
    path('especialidades/crear/', EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('especialidades/<int:pk>/editar/', EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidades/<int:pk>/eliminar/', EspecialidadDeleteView.as_view(), name='especialidad_delete'),
    
    # 👨‍⚕️ CRUD Doctores
    path('doctores/', DoctorListView.as_view(), name='doctor_list'),
    path('doctores/crear/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/<int:pk>/editar/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/<int:pk>/eliminar/', DoctorDeleteView.as_view(), name='doctor_delete'),
    
     # 👷 Empleados
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/<int:pk>/eliminar/', EmpleadoDeleteView.as_view(), name='empleado_delete'),

    # 📋 Cargos
    path('cargos/', CargoListView.as_view(), name='cargo_list'),
    path('cargos/crear/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/<int:pk>/editar/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/<int:pk>/eliminar/', CargoDeleteView.as_view(), name='cargo_delete'),
]
   