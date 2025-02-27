# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politicas_afirmativas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidodeisencaouerj',
            options={'managed': True, 'verbose_name': 'Isen\xe7\xe3o de Inscri\xe7\xe3o UERJ', 'verbose_name_plural': 'Isen\xe7\xf5es de Inscri\xe7\xe3o UERJ'},
        ),
        migrations.AlterField(
            model_name='pedidodeisencaouerj',
            name='typeof_residencia',
            field=models.CharField(blank=True, choices=[('Luz', 'Luz'), ('\xc1gua', '\xc1gua'), ('G\xe1s', 'G\xe1s'), ('Telefone', 'Telefone fixo ou internet fixa'), ('Celular', 'Telefone celular ou internet m\xf3vel'), ('TV por assinatura', 'TV'), ('Cart\xe3o de cr\xe9dito', 'Cart\xe3o de Cr\xe9dito'), ('Outra', 'Outra')], max_length=10, null=True, verbose_name='Tipo de comprovante de resid\xeancia'),
        ),
        migrations.AlterField(
            model_name='pedidodeisencaouerj',
            name='typeof_rg',
            field=models.CharField(blank=True, choices=[('ID civil', 'Identidade civil'), ('ID militar', 'Identidade militar'), ('CNH', 'Carteira de motorista'), ('CHP', 'Carteira de habilita\xe7\xe3o profissional'), ('Outro', 'Outro')], max_length=10, null=True, verbose_name='Tipo de identidade'),
        ),
    ]
