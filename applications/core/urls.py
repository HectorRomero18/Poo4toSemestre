from django.urls import path
from applications.core.views.paciente import paciente_find, PacienteCreateView, PacienteListView, PacienteUpdateView, PacienteDeleteView

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
    path('paciente_find/', paciente_find, name="paciente_find"),
    path('pacientes_list/', PacienteListView.as_view(), name="pacientes_list"),
    path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    path('paciente_update/<int:pk>/', PacienteUpdateView.as_view(), name="paciente_update"),
    path('paciente_delete/<int:pk>/', PacienteDeleteView.as_view(), name="paciente_delete"),
    # ... otras rutas ...

]