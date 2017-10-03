# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Usuario(models.Models):
    """
    """

    nome = models.CharField(
        label='Nome',
        max_lenght=60,
        null=False,
        blank=False
    )

    email = models.EmailField(
        label='Email',
        max_lenght=100,
        null=False,
        blank=False
    )

    senha = models.CharField(
        label='Senha',
        max_lenght=50,
        null=False,
        blank=False
    )

    professor = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

class Turma(models.Models):
    """
    """

    nome = models.CharField(
        label='Nome',
        max_lenght=60,
        null=False,
        blank=False
    )

    horario = models.DateTimeField(
        null=False,
        blank=False
    )

    professor = models.ForeignKey(
        Usuario,
        blank=False,
        null=False
    )

class Empresa(models.Models):
    """
    """

class Atividade(models.Models):
    """
    """
