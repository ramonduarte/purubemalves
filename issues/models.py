# coding=utf-8
from __future__ import unicode_literals
from website import models as wm
from django.db import models
from django.contrib.postgres import fields


class Issue(models.Model):
    # GitHub API attributes
    number = models.IntegerField(primary_key=True, verbose_name=u'Número')
    title = models.CharField(max_length=wm.superlongfield, verbose_name=u'Título')
    body = models.CharField(max_length=wm.superlongfield*10, blank=True, null=True, verbose_name=u'Descrição')
    assignee = models.ForeignKey(wm.Voluntario, blank=True, null=True,
                                 related_name=u'Responsavel', verbose_name=u'Responsável')
    is_closed = models.BooleanField(default=False, verbose_name=u'Encerrado')
    close_date = models.DateField(null=True, blank=True, verbose_name=u'Data de encerramento')
    creation_date = models.DateField(null=True, blank=True, verbose_name=u'Data de criação')
    milestone = models.ForeignKey('Milestone', verbose_name=u'Versão alvo')

    # purubemalves attributes
    submitter = models.ForeignKey(wm.Voluntario, related_name=u'Autor', verbose_name=u'Autor')
    labels = fields.ArrayField(models.CharField(max_length=wm.shortfield, choices=(
        (u'Dúvida', u'question'),
        (u'Reclamação', u'complaint'),
        (u'Bug (falha imprevista)', u'bug'),
        (u'Melhoramento', u'enhancement'),
        (u'Sugestão de novidade', u'feature'),
        (u'Baixa prioridade', u'low priority'),
        (u'Média prioridade', u'medium priority'),
        (u'Alta prioridade', u'high priority'),
        (u'Duplicata', u'duplicate'),
        (u'Sem validade', u'invalid'),
        (u'Sem conserto', u'wontfix'),
    ),
                                                verbose_name=u'Etiqueta'))

    def __unicode__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = u'Ticket'
        verbose_name_plural = u'Tickets'


class Milestone(models.Model):
    # GitHub API attributes
    target_date = models.DateField(null=True, blank=True, verbose_name=u'Data alvo')
    name = models.CharField(max_length=wm.longfield, verbose_name=u'Nome')
    is_open = models.BooleanField(default=True, verbose_name=u'Aberto')
    last_updated = models.DateField(null=True, blank=True, verbose_name=u'Última atualização')

    def __unicode__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = u'Atualização'
        verbose_name_plural = u'Atualizações'
