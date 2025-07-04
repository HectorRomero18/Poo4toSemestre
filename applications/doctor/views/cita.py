from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.views.generic import ListView, CreateView
from applications.doctor.models import CitaMedica
from applications.doctor.forms.cita import CitaMedicaForm
from applications.security.components.mixin_crud import PermissionMixin, CreateViewMixin, ListViewMixin

class CitaMedicaListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/citas/lista.html'
    model = CitaMedica
    context_object_name = 'citas'
    permission_required = 'view_citamedica'

    def get_queryset(self):
        return self.model.objects.all().order_by('fecha', 'hora_cita')

class CitaMedicaCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = CitaMedica
    template_name = 'doctor/citas/form.html'
    form_class = CitaMedicaForm
    success_url = reverse_lazy('doctor:cita_list')
    permission_required = 'add_citamedica'

    def form_valid(self, form):
        # Validación: no permitir doble cita en el mismo horario
        fecha = form.cleaned_data['fecha']
        hora = form.cleaned_data['hora_cita']
        doctor = form.cleaned_data['doctor']
        if CitaMedica.objects.filter(fecha=fecha, hora_cita=hora, doctor=doctor).exists():
            form.add_error(None, "Ya existe una cita para ese doctor en ese horario.")
            return self.form_invalid(form)
        with transaction.atomic():
            self.object = form.save()
            messages.success(self.request, "Cita agendada correctamente.")
            return super().form_valid(form)