# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple, RelatedFieldWidgetWrapper
from django.contrib import admin

from go.models import *

def add_related_field_wrapper(form, col_name):
    rel_model = form.Meta.model
    rel = rel_model._meta.get_field(col_name).rel
    form.fields[col_name].widget = RelatedFieldWidgetWrapper(form.fields[col_name].widget, rel, admin.site, can_add_related=True, can_change_related=True)

class EmpresaForm(forms.ModelForm):
    alunos = forms.ModelChoiceField(queryset=Usuario.objects.all())

    class Meta:
        model = Empresa
        fields = ('nome', 'turma', 'descricao', 'alunos')
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'turma': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(EmpresaForm, self).__init__(*args, **kwargs)
        add_related_field_wrapper(self, 'alunos')
            

class AtividadeForm(forms.ModelForm):

    turma = forms.ModelChoiceField(queryset=Turma.objects.all())

    data_entrega = forms.DateField(widget = forms.SelectDateWidget)

    class Meta:
        model = Atividade
        fields = ('titulo', 'descricao', 'turma', 'data_entrega')
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'turma': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control'}
            )
        }


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentario',)
        widgets = {
            'comentario': forms.Textarea(
                attrs={'placeholder': 'Escreva aqui um comentario...',
                       'class': 'form-control'}
            ),
        }


class TrabalhoAtividadeForm(forms.ModelForm):

    class Meta:
        model = TrabalhoAtividade
        fields = ('arquivo',)


class NotaTrabalhoAtividadeForm(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ('nota',)
        widgets = {
            'nota': forms.TextInput(
                attrs={'placeholder': 'Nota',
                       'class': 'form-control'}
            ),
        }