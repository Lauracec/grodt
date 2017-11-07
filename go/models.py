# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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

class Comentario(models.Model):
    """
    """

    comentario = models.TextField()

    data = models.DateTimeField()

    autor = models.ForeignKey(Usuario)

    atividade = models.ForeignKey(Atividade)