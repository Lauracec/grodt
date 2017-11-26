from django.conf.urls import url, include
from django.contrib import admin

from go import views

urlpatterns = [
    url(r'^$', views.portal, name='inicio_portal'),
    url(r'^turma/$', views.turma, name='turma'),
    url(r'^empresa/$', views.empresa, name='empresa'),
    url(r'^empresa/(?P<pk>[/0-9]+)/$', views.detalhes_empresa, name='detalhes_empresa'),
    url(r'^atividades/$', views.atividades, name='atividades'),
    url(r'^atividades/(?P<pk>[/0-9]+)/$', views.detalhes_atividade, name='detalhes_atividade'),
    url(r'^conquistas/$', views.conquistas, name='conquistas'),
]
