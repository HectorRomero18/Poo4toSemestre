from django.shortcuts import render

def vista_calendario(request):
    return render(request, 'core/calendario.html')
