# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from go.models import *
from go.forms import *

# Create your views here.

def login(request):
    return render(request, 'login.html')

@login_required
def portal(request):
    return render(request, 'portal-inicio.html')

@login_required
def turma(request):
    try:
        turma = Turma.objects.get(participantes__pk=request.user.pk)
        turma.professor = turma.participantes.get(professor=True)
        turma.alunos = turma.participantes.filter(professor=False)
    except:
        turma = ''
    return render(request, 
                  'turma.html',
                  {'turma': turma})

@login_required
def empresa(request):
    try:
        empresa = Empresa.objects.get(alunos__pk=request.user.pk)
    except:
        empresa = ''
    empresas = Empresa.objects.all()
    return render(request, 
                  'empresa.html',
                  {'empresa': empresa,
                   'empresas': empresas})

@login_required
def atividades(request):
    try:
        turma = Turma.objects.get(participantes__pk=request.user.pk)
        atividades = Atividade.objects.filter(turma=turma)
    except:
        atividades = ''
    return render(request, 
                  'atividades.html',
                  {'atividades': atividades})

@login_required
def detalhes_atividade(request, pk):
    atividade = Atividade.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(atividade__pk=pk)    
    autor = Usuario.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.atividade = atividade
            post.autor = Usuario.objects.get(pk=request.user.pk)
            post.data = timezone.now()
            post.save()
    form = ComentarioForm()
    return render(request, 
                  'detalhes-atividade.html',
                  {'atividade': atividade,
                   'comentarios': comentarios,
                   'form': form})

