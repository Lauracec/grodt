# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class Usuario(User):
    """
    """

    professor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

    class Meta:
        ordering = ['username']


class Turma(models.Model):
    """
    """

    nome = models.CharField(max_length=60)

    data_inicio = models.DateField()

    data_fim = models.DateField()

    horario = models.CharField(max_length=20)

    participantes = models.ManyToManyField(Usuario)

    data_inicio = models.DateField(
        'Data de Início',
        null=True,
        blank=True
    )

    data_fim = models.DateField(
        'Data de Encerramento',
        null=True,
        blank=True
    )

    horario = models.TimeField()

    def __unicode__(self):
        return self.nome


class Empresa(models.Model):
    """
    """

    nome = models.CharField(max_length=60)

    turma = models.ForeignKey(Turma)

    descricao = models.TextField()

    alunos = models.ManyToManyField(Usuario)

    def __unicode__(self):
        return self.nome


class Atividade(models.Model):
    """
    """

    titulo = models.CharField(max_length=60)

    descricao = models.TextField()

    turma = models.ForeignKey(Turma)

    data_entrega = models.DateTimeField()

    def __unicode__(self):
        return self.titulo

    def aberta(self):
        return self.data_entrega > timezone.now()

    class Meta:
        ordering = ['-data_entrega']


class TrabalhoAtividade(models.Model):

    atividade = models.ForeignKey(Atividade)

    usuario = models.ForeignKey(Usuario)

    empresa = models.ForeignKey(Empresa)

    data_upload = models.DateTimeField(auto_now_add=True)

    arquivo = models.FileField(upload_to='media/')


class Comentario(models.Model):
    """
    """
    comentario = models.TextField()

    data = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(Usuario)

    trabalho_atividade = models.ForeignKey(TrabalhoAtividade)


class Nota(models.Model):
    """
    """
    nota = models.FloatField(null=True,blank=True)

    trabalho_atividade = models.ForeignKey(TrabalhoAtividade)
