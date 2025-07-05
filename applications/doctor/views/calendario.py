from django.shortcuts import render

def calendario(request):
    return render(request, 'doctor/citas/calendario.html')