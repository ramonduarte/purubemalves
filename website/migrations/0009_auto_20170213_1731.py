# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20170213_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.BigIntegerField(),
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='curso_pretendido',
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso_pretendido',
            field=models.ManyToManyField(blank=True, to='website.Curso'),
        ),
        migrations.AlterField(
            model_name='voluntario',
            name='cpf',
            field=models.BigIntegerField(),
        ),
    ]
