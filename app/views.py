from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from . import forms
from django.shortcuts import render, redirect
# Create your views here.
def index(request):
    area = models.Area.objects.all()
    paginator = Paginator(area, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)
    context = {
        'area': page_obj
    }
    return render(request, 'app/index.html', context)

def inicial(request):
    return render(request, 'app/inicial.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def cursos(request, area_id):
    area = models.Area.objects.get(id=area_id)
    cursos = models.Curso.objects.filter(area=area)
    context = {
        'area': area,
        'cursos': cursos
    }
    return render(request, 'app/cursos.html', context)

def cadastro_curso(request):
    if request.method == 'POST':
        form = forms.CursosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos', area_id=form.cleaned_data['area'].id)
        
    else:
        form = forms.CursosForm()
    
    return render(request, 'app/cadastro_curso.html', {'form': form},)

def editar_curso(request, id):
    curso = models.Curso.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CursosForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos', area_id=form.cleaned_data['area'].id)
        
    else:
        form = forms.CursosForm()
    form = forms.CursosForm(instance=curso)
    


    return render(request, 'app/cadastro_curso.html', {'form': form},)

def deletar_curso(request, id):
    curso = models.Curso.objects.get(id=id)
    area_id = curso.area.id
    curso.delete()
    return redirect('cursos', area_id=area_id)