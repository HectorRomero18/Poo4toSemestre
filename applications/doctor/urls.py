from django.urls import path

from applications.doctor.views.atencion_medica import AtencionListView, AtencionCreateView, AtencionUpdateView, \
    AtencionDeleteView
from applications.doctor.views.pago import PagoListView, PagoCreateView, PagoDeleteView, PagoUpdateView
from applications.doctor.views.detalles_pago import DetallePagoCreateView, DetallePagoUpdateView, DetallePagoDetailView
from applications.doctor.views.servicios_adicionales import ServiciosAdicionalesListView, ServiciosAdicionalesCreateView, ServiciosAdicionalesUpdateView, ServiciosAdicionalesDeleteView
from applications.doctor.views.paypal import pago_paypal, pago_cancelado, pago_exitoso
from applications.doctor.views.calendario import calendario

from applications.doctor.views.horario import HorarioAtencionCreateView, HorarioAtencionDeleteView, HorarioAtencionListView, HorarioAtencionUpdateView
from applications.doctor.views import cita
from applications.doctor.views.atencion import ver_detalle_atencion
from applications.doctor.views.receta import receta_imprimir
from applications.doctor.views.detalle_atencion_views import (
    DetalleAtencionListView, DetalleAtencionCreateView, DetalleAtencionUpdateView, DetalleAtencionDeleteView,
    guardar_detalle_atencion  # Import the view here
)
from applications.doctor.views.cita import CitaMedicaListView, CitaMedicaCreateView


app_name='doctor' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Doctor
    path('atencion_list/', AtencionListView.as_view(), name="atencion_list"),
    path('atencion_create/', AtencionCreateView.as_view(), name="atencion_create"),
    path('atencion_update/<int:pk>/', AtencionUpdateView.as_view(), name="atencion_update"),
    path('atencion_delete/<int:pk>/', AtencionDeleteView.as_view(), name="atencion_delete"),

    # rutas para vistas relacionadas con el Pago
    path('pago_list/', PagoListView.as_view(), name="pago_list"),
    path('pago_create/', PagoCreateView.as_view(), name="pago_create"),
    path('pago_delete/<int:pk>/', PagoDeleteView.as_view(), name="pago_delete"),
    path('pago_update/<int:pk>/', PagoUpdateView.as_view(), name="pago_update"),
    
    # ruta para DetallePago
    path('detalle_pago_create/', DetallePagoCreateView.as_view(), name="detalle_pago_create"),
    path('detalle_pago_update/<int:pk>/', DetallePagoUpdateView.as_view(), name="detalle_pago_update"),
    path('detalle_pago/<int:pk>/', DetallePagoDetailView.as_view(), name='detalle_pago_detail'),


    # Rutas para el Modelo de ServiciosAdicionales
    path('servicios_list/', ServiciosAdicionalesListView.as_view(), name="servicios_list"),
    path('servicios_create/', ServiciosAdicionalesCreateView.as_view(), name="servicios_create"),
    path('servicio_update/<int:pk>/', ServiciosAdicionalesUpdateView.as_view(), name="servicio_update"),
    path('servicio_delete/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(), name="servicio_delete"),


    # Rutas para el modelo Horarios
    path('horarios_list/', HorarioAtencionListView.as_view(), name="horarios_list"),
    path('horarios_create/', HorarioAtencionCreateView.as_view(), name="horarios_create"),
    path('horario_update/<int:pk>/', HorarioAtencionUpdateView.as_view(), name="horario_update"),
    path('horario_delete/<int:pk>/', HorarioAtencionDeleteView.as_view(), name="horario_delete"),


    # Rutas para pagar con paypal
    
    path('pagos/paypal/<int:monto>/<int:atencion_id>/', pago_paypal, name='pago_paypal'),
    path('pago-exitoso/', pago_exitoso, name='pago_exitoso'),
    path('pago-cancelado/', pago_cancelado, name='pago_cancelado'),

    path('atencion/<int:atencion_id>/detalle/', ver_detalle_atencion, name='detalle_atencion'),
    path('receta/<int:detalle_id>/imprimir/', receta_imprimir, name='receta_imprimir'),
    path('receta/atencion/<int:atencion_id>/imprimir/', receta_imprimir, name='receta_atencion_imprimir'),

    path('detalle_atencion_list/', DetalleAtencionListView.as_view(), name="detalle_atencion_list"),
    path('detalle_atencion_create/', DetalleAtencionCreateView.as_view(), name="detalle_atencion_create"),
    path('detalle_atencion_update/<int:pk>/', DetalleAtencionUpdateView.as_view(), name="detalle_atencion_update"),
    path('detalle_atencion_delete/<int:pk>/', DetalleAtencionDeleteView.as_view(), name="detalle_atencion_delete"),
    path('cita_medica_list/', CitaMedicaListView.as_view(), name="cita_medica_list"),
    path('cita_medica_create/', CitaMedicaCreateView.as_view(), name="cita_medica_create")
]