# -*- coding: utf-8 -*-
from django import forms
from go.models import *

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