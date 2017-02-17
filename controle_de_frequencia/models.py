# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from website import models as wm
import datetime


class ListaDePresenca(models.Model):
    data = models.DateField(default=datetime.date.today)
    obs = models.CharField(max_length=wm.longfield, blank=True, null=True, verbose_name=u'Observações')

    def get_data(self):
        return self.data

    def __unicode__(self):
        return unicode(self.data)

    class Meta:
        managed = True
        abstract = True


class ListaDePresencaDeVoluntarios(ListaDePresenca):
    voluntario = models.ManyToManyField(wm.Voluntario)

    def get_voluntario(self):
        return [self.voluntario.all()[i] for i in range(len(self.voluntario.all()))]

    class Meta:
        managed = True
        # ordering = ('voluntario',)
        verbose_name = 'Lista de Presença de Voluntários'
        verbose_name_plural = 'Listas de Presença de Voluntários'


class ListaDePresencaDeAlunos(ListaDePresenca):
    aluno = models.ManyToManyField(wm.Aluno)

    def get_aluno(self):
        return [self.aluno.all()[i] for i in range(len(self.aluno.all()))]

    class Meta:
        managed = True
        # ordering = ('aluno',)
        verbose_name = 'Lista de Presença de Alunos'
        verbose_name_plural = 'Listas de Presença de Alunos'
