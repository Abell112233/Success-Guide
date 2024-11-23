from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    area = models.Area.objects.all()
    context = {
        'area': area
    }
    return render(request, 'app/index.html', context)

def inicial(request):
    return render(request, 'app/inicial.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def cursos(request):
    cursos = models.Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'app/cursos.html', context)