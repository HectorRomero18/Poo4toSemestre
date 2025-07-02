from django.urls import path
from applications.core.views.paciente import paciente_find, PacienteCreateView

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
    path('paciente_find/', paciente_find, name="paciente_find"),
     path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    # ... otras rutas ...

]