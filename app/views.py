from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from . import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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

@login_required
def perfil(request):
    return render(request, 'app/perfil.html')

@login_required
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

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'app/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('inicial')

def register_usuario(request):
    if request.method == 'POST':
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('login_usuario')
    else:
        form = forms.UsuarioForm()

    return render(request, 'app/register.html', {'form': form})

def areas(request):
    filtro = forms.FiltroForm(request.GET or None)

    areas = models.Area.objects.all()

    if filtro.is_valid():
        if filtro.cleaned_data['nome']:
            areas = areas.filter(nome__icontains=filtro.cleaned_data['nome'])


    contexto = {
        'areas': areas,
        'filtro': filtro
    }
    return render(request, 'app/areas.html', contexto)
