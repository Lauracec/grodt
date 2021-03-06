# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='data_fim',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_inicio',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turma',
            name='horario',
            field=models.CharField(max_length=20),
        ),
    ]
