from django.urls import path

from applications.doctor.views.atencion_medica import AtencionListView, AtencionCreateView, AtencionUpdateView, \
    AtencionDeleteView
from applications.doctor.views.pago import PagoListView, PagoCreateView, PagoDeleteView, PagoUpdateView
from applications.doctor.views.detalles_pago import DetallePagoCreateView, DetallePagoUpdateView
from applications.doctor.views.servicios_adicionales import ServiciosAdicionalesListView, ServiciosAdicionalesCreateView, ServiciosAdicionalesUpdateView, ServiciosAdicionalesDeleteView
from applications.doctor.views.paypal import pago_paypal, pago_cancelado, pago_exitoso

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

    # Rutas para el Modelo de ServiciosAdicionales
    path('servicios_list/', ServiciosAdicionalesListView.as_view(), name="servicios_list"),
    path('servicios_create/', ServiciosAdicionalesCreateView.as_view(), name="servicios_create"),
    path('servicio_update/<int:pk>/', ServiciosAdicionalesUpdateView.as_view(), name="servicio_update"),
    path('servicio_delete/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(), name="servicio_delete"),

    # Rutas para pagar con paypal
    
    path('pagos/paypal/<int:monto>/<int:atencion_id>/', pago_paypal, name='pago_paypal'),
    path('pago-exitoso/', pago_exitoso, name='pago_exitoso'),
    path('pago-cancelado/', pago_cancelado, name='pago_cancelado'),

    

]