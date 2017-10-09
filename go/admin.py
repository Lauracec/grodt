# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from go import models

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (u'nome', u'email', u'professor')

admin.site.register(models.Usuario, UsuarioAdmin)

admin.autodiscover()
