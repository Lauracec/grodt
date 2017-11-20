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
    return render(request, 'portal_inicio.html')

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

    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
    form = AtividadeForm()
    try:
        turma = Turma.objects.get(participantes__pk=request.user.pk)
        atividades = Atividade.objects.filter(turma=turma)
    except:
        atividades = ''
    return render(request,
                  'atividades.html',
                  {'atividades': atividades,
                   'form': form})

@login_required
def detalhes_atividade(request, pk):
    atividade = Atividade.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(trabalho_atividade__pk=pk)
    trabalhos = TrabalhoAtividade.objects.filter(atividade__pk=pk)
    try:
        nota = Nota.objects.get(trabalho_atividade__pk=pk)
    except:
        nota = ''
    try:
        trabalho_entregue = trabalhos.get(empresa__alunos=request.user.pk)
    except:
        trabalho_entregue = ''

    usuario = Usuario.objects.get(pk=request.user.pk)

    if 'comentario' in request.POST:
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            post = form_comentario.save(commit=False)
            post.trabalho_atividade = TrabalhoAtividade.objects.get(pk=request.POST['comentario_trabalho_pk'])
            #post.autor = Usuario.objects.get(pk=request.user.pk)
            post.autor = usuario
            post.save()
    form_comentario = ComentarioForm()

    if 'arquivo' in request.FILES:
        form_trabalho = TrabalhoAtividadeForm(request.POST, request.FILES)

        if form_trabalho.is_valid():
            post = form_trabalho.save(commit=False)
            post.atividade = atividade
            #post.usuario = Usuario.objects.get(pk=request.user.pk)
            post.usuario = usuario
            post.empresa = Empresa.objects.get(alunos__pk=request.user.pk)
            post.arquivo = request.FILES['arquivo']
            post.save()
    form_trabalho = TrabalhoAtividadeForm()

    if 'nota' in request.POST:
        form_nota = NotaTrabalhoAtividadeForm(request.POST)

        if form_nota.is_valid():
            post = form_nota.save(commit=False)
            post.trabalho_atividade = TrabalhoAtividade.objects.get(pk=request.POST['nota_trabalho_pk'])
            post.save()
    form_nota = NotaTrabalhoAtividadeForm()

    return render(request,
                  'detalhes_atividade.html',
                  {'atividade': atividade,
                   'trabalhos': trabalhos,
                   'comentarios': comentarios,
                   'form_comentario': form_comentario,
                   'form_trabalho': form_trabalho,
                   'form_nota': form_nota,
                   'trabalho_entregue': trabalho_entregue,
                   'nota': nota})
