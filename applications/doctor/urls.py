from django.urls import path

from applications.doctor.views.atencion_medica import AtencionListView, AtencionCreateView, AtencionUpdateView, \
    AtencionDeleteView

from applications.doctor.views import horario
from applications.doctor.views import cita


app_name='doctor' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Doctor
    path('atencion_list/', AtencionListView.as_view(), name="atencion_list"),
    path('atencion_create/', AtencionCreateView.as_view(), name="atencion_create"),
    path('atencion_update/<int:pk>/', AtencionUpdateView.as_view(), name="atencion_update"),
    path('atencion_delete/<int:pk>/', AtencionDeleteView.as_view(), name="atencion_delete"),
    path('horarios/', horario.HorarioAtencionListView.as_view(), name='horario_list'),
    path('horarios/nuevo/', horario.HorarioAtencionCreateView.as_view(), name='horario_create'),
    path('horarios/<int:pk>/editar/', horario.HorarioAtencionUpdateView.as_view(), name='horario_edit'),
    path('horarios/<int:pk>/eliminar/', horario.HorarioAtencionDeleteView.as_view(), name='horario_delete'),
    path('citas/', cita.CitaMedicaListView.as_view(), name='cita_list'),
    path('citas/nueva/', cita.CitaMedicaCreateView.as_view(), name='cita_create'),
]