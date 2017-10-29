# -*- coding: utf-8 -*-
from django import forms
from go.models import *

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentario',)
        widgets = {
            'comentario': forms.Textarea(
            	attrs={'placeholder': 'Escreva aqui um comentario...'}
            ),
        }

#class NotaAtividadeForm(forms.ModelForm):
#
#    class Meta:
#        model = Atividade
#        fields = ('nota',)
#        widgets = {
#            'nota': forms.CharField(
#            	attrs={'placeholder': 'Nota'}
#            ),
#        }