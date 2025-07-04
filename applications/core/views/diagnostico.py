from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Diagnostico
from applications.core.forms.diagnostico import DiagnosticoForm

class DiagnosticoListView(ListView):
    model = Diagnostico
    template_name = 'core/diagnostico/lista.html'
    context_object_name = 'diagnosticos'

class DiagnosticoCreateView(CreateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'core/diagnostico/form.html'
    success_url = reverse_lazy('core:diagnostico_list')

class DiagnosticoUpdateView(UpdateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'core/diagnostico/form.html'
    success_url = reverse_lazy('core:diagnostico_list')

class DiagnosticoDeleteView(DeleteView):
    model = Diagnostico
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:diagnostico_list')