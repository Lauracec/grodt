# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone

from go.models import *
from go.forms import *

# Create your views here.

def login(request):
    return render(request, 'login.html')

def portal(request):
    return render(request, 'portal-inicio.html')

def turma(request):
    # participantes__pk=request.user
    turma = Turma.objects.get(participantes__pk=1)
    turma.professor = turma.participantes.get(professor=True)
    turma.alunos = turma.participantes.filter(professor=False)
    return render(request, 
                  'turma.html',
                  {'turma': turma})

def empresa(request):
    # alunos__pk=request.user
    empresa = Empresa.objects.get(alunos__pk=1)
    return render(request, 
                  'empresa.html',
                  {'empresa': empresa})

def atividades(request):
    # participantes__pk=request.user
    turma = Turma.objects.get(participantes__pk=1)
    atividades = Atividade.objects.filter(turma=turma)
    return render(request, 
                  'atividades.html',
                  {'atividades': atividades})

def detalhes_atividade(request, pk):
    atividade = Atividade.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(atividade__pk=pk)    
    autor = Usuario.objects.get(pk=1)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.atividade = atividade
            # autor=request.user
            post.autor = autor
            post.data = timezone.now()
            post.save()
    form = ComentarioForm()
    return render(request, 
                  'detalhes-atividade.html',
                  {'atividade': atividade,
                   'comentarios': comentarios,
                   'form': form})

