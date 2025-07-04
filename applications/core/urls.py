from django.urls import path
from applications.core.views.paciente import paciente_find, PacienteCreateView,PacienteDeleteView, PacienteUpdateView, PacienteListView
from applications.core.views.diagnostico import DiagnosticoCreateView, DiagnosticoListView, DiagnosticoDeleteView, DiagnosticoUpdateView
from django.urls import path
from applications.core.views.calendario import vista_calendario

from applications.core.views.citas import (
    citas_json,
    crear_cita,
    mover_cita,
    verificar_paciente,
    verificar_disponibilidad,
)
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
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

    



]