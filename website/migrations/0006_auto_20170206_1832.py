# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 20:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170206_1831'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ementa',
            options={'managed': False, 'ordering': ('disciplina',)},
        ),
    ]
