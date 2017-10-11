# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Usuario(models.Model):
    """
    """

    nome = models.CharField(max_length=60)

    email = models.EmailField(max_length=100)

    senha = models.CharField(max_length=50)

    professor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

class Turma(models.Model):
    """
    """

    nome = models.CharField(max_length=60)

    horario = models.DateTimeField()

    professor = models.ForeignKey(Usuario)

    def __unicode__(self):
        return self.nome

class Empresa(models.Model):
    """
    """

    nome = models.CharField(max_length=60)

    turma = models.ForeignKey(Turma)

    descricao = models.TextField()

    def __unicode__(self):
        return self.nome

class Atividade(models.Model):
    """
    """

    titulo = models.CharField(max_length=60)

    descricao = models.TextField()

    turma = models.ForeignKey(Turma)

    professor = models.ForeignKey(Usuario)

    nota = models.FloatField()

    def __unicode__(self):
        return self.nome
