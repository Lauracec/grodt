# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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

    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('empresa'))
    form = EmpresaForm()

    empresas = Empresa.objects.all()
    return render(request,
                  'empresa.html',
                  {'empresa': empresa,
                   'empresas': empresas,
                   'form': form})

@login_required
def detalhes_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)

    return render(request,
                  'detalhes_empresa.html',
                  {'empresa': empresa})

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
    atividade = get_object_or_404(Atividade, pk=pk)
    #comentarios = Comentario.objects.filter(trabalho_atividade__pk=pk)
    trabalhos = TrabalhoAtividade.objects.filter(atividade__pk=pk)
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
            return HttpResponseRedirect(reverse('detalhes_atividade', args=[pk]))
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
            return HttpResponseRedirect(reverse('detalhes_atividade', args=[pk]))
    form_trabalho = TrabalhoAtividadeForm()

    if 'nota' in request.POST:
        form_nota = NotaTrabalhoAtividadeForm(request.POST)

        if form_nota.is_valid():
            post = form_nota.save(commit=False)
            post.trabalho_atividade = TrabalhoAtividade.objects.get(pk=request.POST['nota_trabalho_pk'])
            post.save()
            return HttpResponseRedirect(reverse('detalhes_atividade', args=[pk]))
    form_nota = NotaTrabalhoAtividadeForm()

    return render(request,
                  'detalhes_atividade.html',
                  {'atividade': atividade,
                   'trabalhos': trabalhos,
                   'form_comentario': form_comentario,
                   'form_trabalho': form_trabalho,
                   'form_nota': form_nota,
                   'trabalho_entregue': trabalho_entregue})

@login_required
def conquistas(request):
    conquista_1 = False
    conquista_2 = False
    conquista_3 = False
    conquista_4 = False
    pontos = 0
    contador_atividades = 0

    conquistas = Conquista.objects.all()

    try:
        empresa = Empresa.objects.get(alunos__pk=request.user.pk)
        empresa_membros = empresa.alunos.count()
        if empresa_membros > 4:
            conquista_1 = True
            pontos = pontos + 100
    except:
        empresa = ''

    atividades = Atividade.objects.all()
    for atividade in atividades:
        try:
            atividade_empresa = atividade.trabalhoatividade_set.get(empresa=empresa)
            contador_atividades = contador_atividades + 1
            if atividade_empresa.nota_set.first().nota == 10:
                conquista_4 = True
                pontos = pontos + 300
        except:
            pass

    if contador_atividades:
        conquista_2 = True
        pontos = pontos + 100 + contador_atividades*50
    
    if contador_atividades > 5:
        conquista_3 = True
        pontos = pontos + 200

    #from IPython import embed;embed()

    niveis = Nivel.objects.filter(pontos_minimos__gte=pontos)
    niveis.progresso = pontos*100/niveis[1].pontos_minimos

    return render(request,
                'conquistas.html',
                {'conquistas': conquistas,
                 'conquista_1': conquista_1,
                 'conquista_2': conquista_2,
                 'conquista_3': conquista_3,
                 'conquista_4': conquista_4,
                 'pontos': pontos,
                 'niveis': niveis})