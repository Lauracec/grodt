# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0004_trabalhoatividade_nota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='trabalhoatividade',
            name='nota',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='nota',
            name='trabalho_atividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='go.TrabalhoAtividade'),
        ),
    ]
