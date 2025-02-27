# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 23:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidodeinscricao',
            name='ano_letivo',
            field=models.IntegerField(default=2017, verbose_name='Ano letivo'),
        ),
        migrations.AddField(
            model_name='pedidodeinscricao',
            name='data_de_inscricao',
            field=models.DateField(default=datetime.date.today, verbose_name='Data de Inscri\xe7\xe3o'),
        ),
        migrations.AddField(
            model_name='pedidodeinscricao',
            name='obs',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observa\xe7\xf5es'),
        ),
        migrations.AddField(
            model_name='pedidodeinscricao',
            name='turma',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], default='A', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pedidodeinscricao',
            name='data_do_pedido',
            field=models.DateField(default=datetime.date.today, verbose_name='Data do Pedido'),
        ),
    ]
