# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 20:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20170206_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'managed': False, 'ordering': ('nome',)},
        ),
        migrations.AlterModelOptions(
            name='equipe',
            options={'managed': False, 'ordering': ('nome',)},
        ),
        migrations.AlterModelOptions(
            name='voluntario',
            options={'managed': False, 'ordering': ('nome',), 'verbose_name': 'Volunt\xe1rio', 'verbose_name_plural': 'Volunt\xe1rios'},
        ),
    ]
