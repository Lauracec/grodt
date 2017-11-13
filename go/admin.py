# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from go import models

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (u'username', u'email', u'professor',)

class TurmaAdmin(admin.ModelAdmin):
    list_display = (u'nome', u'professor', u'data_inicio', u'data_fim',
        u'horario')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = (u'nome', u'turma', u'descricao')

class AtividadeAdmin(admin.ModelAdmin):
    list_display = (u'titulo', u'descricao', u'turma')

class TrabalhoAtividadeAdmin(admin.ModelAdmin):
    list_display = (u'atividade', u'empresa')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = (u'comentario', u'autor')

class NotaAdmin(admin.ModelAdmin):
    list_display = (u'trabalho_atividade', u'nota')

admin.site.register(models.Usuario, UsuarioAdmin)
admin.site.register(models.Turma, TurmaAdmin)
admin.site.register(models.Empresa, EmpresaAdmin)
admin.site.register(models.Atividade, AtividadeAdmin)
admin.site.register(models.TrabalhoAtividade, TrabalhoAtividadeAdmin)
admin.site.register(models.Comentario, ComentarioAdmin)
admin.site.register(models.Nota, NotaAdmin)

admin.autodiscover()
