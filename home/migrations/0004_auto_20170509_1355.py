# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_pedidodeinscricao_is_ativo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidodeinscricao',
            options={'managed': True, 'ordering': ('nome',), 'verbose_name': 'Pedido de Inscri\xe7\xe3o', 'verbose_name_plural': 'Pedidos de Inscri\xe7\xe3o'},
        ),
    ]
