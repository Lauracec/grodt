# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0004_auto_20171125_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='conquista',
            name='icone',
            field=models.CharField(default='cogs', max_length=60),
        ),
    ]
