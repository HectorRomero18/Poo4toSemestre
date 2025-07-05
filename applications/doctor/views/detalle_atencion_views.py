from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from applications.doctor.models import DetalleAtencion
from applications.core.models import Medicamento
from applications.doctor.forms.detalleAtencion import DetalleAtencionForm  # Ensure you have a form for DetalleAtencion

class DetalleAtencionListView(ListView):
    model = DetalleAtencion
    template_name = 'doctor/detalle_atencion_list.html'
    context_object_name = 'detalles'

class DetalleAtencionCreateView(CreateView):
    model = DetalleAtencion
    form_class = DetalleAtencionForm
    template_name = 'doctor/detalle_atencion_form.html'
    success_url = reverse_lazy('doctor:detalle_atencion_list')

class DetalleAtencionUpdateView(UpdateView):
    model = DetalleAtencion
    form_class = DetalleAtencionForm
    template_name = 'doctor/detalle_atencion_form.html'
    success_url = reverse_lazy('doctor:detalle_atencion_list')

class DetalleAtencionDeleteView(DeleteView):
    model = DetalleAtencion
    template_name = 'doctor/detalle_atencion_confirm_delete.html'
    success_url = reverse_lazy('doctor:detalle_atencion_list')
from django.shortcuts import render, redirect

def guardar_detalle_atencion(request):
    if request.method == 'POST':
        form = DetalleAtencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some-view-name')  # Change 'some-view-name' to the name of the view you want to redirect to
    else:
        form = DetalleAtencionForm()
    
    medicamentos = Medicamento.objects.all()
    return render(request, 'doctor/atenciones/form.html', {'form': form, 'medicamentos': medicamentos})
