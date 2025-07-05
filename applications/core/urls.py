from django.urls import path
from applications.core.views.paciente import paciente_find, PacienteCreateView,PacienteDeleteView, PacienteUpdateView, PacienteListView
from applications.core.views.diagnostico import DiagnosticoCreateView, DiagnosticoListView, DiagnosticoDeleteView, DiagnosticoUpdateView

from applications.core.views.paciente import paciente_find, PacienteCreateView
from applications.core.views.tipoSangre import TipoSangreListView, TipoSangreCreateView,TipoSangreUpdateView, TipoSangreDeleteView  
from applications.core.views.especialidad import EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView
from applications.core.views.doctor import DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView
from applications.core.views.empleado import EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView
from applications.core.views.cargo import CargoListView, CargoCreateView, CargoUpdateView, CargoDeleteView
from applications.core.views.views import citas_json, vista_calendario, verificar_disponibilidad, crear_cita, verificar_paciente
from applications.core.views.tipo_medicamento import (
    TipoMedicamentoListView, TipoMedicamentoCreateView,
    TipoMedicamentoUpdateView, TipoMedicamentoDeleteView
)
from applications.core.views.marca_medicamento import (
    MarcaMedicamentoListView, MarcaMedicamentoCreateView,
    MarcaMedicamentoUpdateView, MarcaMedicamentoDeleteView
)
from applications.core.views.medicamento import (
    MedicamentoListView, MedicamentoCreateView,
    MedicamentoUpdateView, MedicamentoDeleteView
)
from applications.core.views.tipo_gasto import (
    TipoGastoListView, TipoGastoCreateView,
    TipoGastoUpdateView, TipoGastoDeleteView,
)
from applications.core.views.gasto_mensual import (
    GastoMensualListView, GastoMensualCreateView,
    GastoMensualUpdateView, GastoMensualDeleteView
)
from applications.core.views.foto_paciente import (
    FotoPacienteListView, FotoPacienteCreateView,
    FotoPacienteUpdateView, FotoPacienteDeleteView
)

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

    path('citas/calendario/json/', vista_calendario, name='cita_calendario_json'),

    # RUTAS PARA TIPO MEDICAMENTO
    path('tipomedicamento_list/', TipoMedicamentoListView.as_view(), name="tipomedicamento_list"),
    path('tipomedicamento_create/', TipoMedicamentoCreateView.as_view(), name="tipomedicamento_create"),
    path('tipomedicamento_update/<int:pk>/', TipoMedicamentoUpdateView.as_view(), name="tipomedicamento_update"),
    path('tipomedicamento_delete/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name="tipomedicamento_delete"),
    # RUTAS PARA MARCA MEDICAMENTO
    path('marcamedicamento_list/', MarcaMedicamentoListView.as_view(), name="marcamedicamento_list"),
    path('marcamedicamento_create/', MarcaMedicamentoCreateView.as_view(), name="marcamedicamento_create"),
    path('marcamedicamento_update/<int:pk>/', MarcaMedicamentoUpdateView.as_view(), name="marcamedicamento_update"),
    path('marcamedicamento_delete/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name="marcamedicamento_delete"),
    # RUTAS PARA MEDICAMENTO
    path('medicamento_list/', MedicamentoListView.as_view(), name="medicamento_list"),
    path('medicamento_create/', MedicamentoCreateView.as_view(), name="medicamento_create"),
    path('medicamento_update/<int:pk>/', MedicamentoUpdateView.as_view(), name="medicamento_update"),
    path('medicamento_delete/<int:pk>/', MedicamentoDeleteView.as_view(), name="medicamento_delete"),
    # RUTAS PARA TIPO GASTO
    path('tipogasto_list/', TipoGastoListView.as_view(), name="tipogasto_list"),
    path('tipogasto_create/', TipoGastoCreateView.as_view(), name="tipogasto_create"),
    path('tipogasto_update/<int:pk>/', TipoGastoUpdateView.as_view(), name="tipogasto_update"),
    path('tipogasto_delete/<int:pk>/', TipoGastoDeleteView.as_view(), name="tipogasto_delete"),
    # RUTAS PARA GASTO MENSUAL
    path('gastomensual_list/', GastoMensualListView.as_view(), name="gastomensual_list"),
    path('gastomensual_create/', GastoMensualCreateView.as_view(), name="gastomensual_create"),
    path('gastomensual_update/<int:pk>/', GastoMensualUpdateView.as_view(), name="gastomensual_update"),
    path('gastomensual_delete/<int:pk>/', GastoMensualDeleteView.as_view(), name="gastomensual_delete"),
     # RUTAS PARA FOTO PACIENTE
    path('fotopaciente_list/', FotoPacienteListView.as_view(), name="fotopaciente_list"),
    path('fotopaciente_create/', FotoPacienteCreateView.as_view(), name="fotopaciente_create"),
    path('fotopaciente_update/<int:pk>/', FotoPacienteUpdateView.as_view(), name="fotopaciente_update"),
    path('fotopaciente_delete/<int:pk>/', FotoPacienteDeleteView.as_view(), name="fotopaciente_delete"),
]