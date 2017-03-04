# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from website import models as wm
import datetime


def avg_grade():
    return 500  # TODO: return average of competencias (2017/02/15)


class ProfessorDeRedacao(models.Model):
    voluntario = models.ForeignKey(wm.Voluntario)

    def get_nome(self):
        return wm.Voluntario.objects.get(pk=self.voluntario_id).nome

    def __unicode__(self):
        return '%s' % (self.get_nome())

    class Meta:
        managed = True
        ordering = ('voluntario',)
        verbose_name = 'Professor de Redação'
        verbose_name_plural = 'Professores de Redação'


class Tema(models.Model):
    titulo = models.CharField(max_length=wm.superlongfield)
    data = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return '%s' % (self.titulo,)

    class Meta:
        managed = True
        ordering = ('data',)
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'


class Redacao(models.Model):
    id = models.AutoField(primary_key=True)
    corretor = models.ManyToManyField(ProfessorDeRedacao)

    def get_corretor(self):
        return [self.corretor.all()[i] for i in range(len(self.corretor.all()))]

    aluno = models.ForeignKey(wm.Aluno)

    def get_aluno(self):
        return self.aluno.nome

    tema = models.ForeignKey(Tema)
    is_devolvida = models.BooleanField(
        default=False,
        verbose_name='Foi devolvida?'
    )
    data_de_entrega = models.DateField(
        verbose_name='Data de entrega',
        default=datetime.date.today,
    )
    data_de_correcao = models.DateField(
        verbose_name='Data de correção',
        default=datetime.date.today,
    )
    data_de_devolucao = models.DateField(
        verbose_name='Data de devolução',
        blank=True, null=True,
    )

    competencia1 = models.FloatField(
        verbose_name='Competência 1',
        blank=True, null=True,
    )
    competencia2 = models.FloatField(
        verbose_name='Competência 2',
        blank=True, null=True,
    )
    competencia3 = models.FloatField(
        verbose_name='Competência 3',
        blank=True, null=True,
    )
    competencia4 = models.FloatField(
        verbose_name='Competência 4',
        blank=True, null=True,
    )
    competencia5 = models.FloatField(
        verbose_name='Competência 5',
        blank=True, null=True,
    )

    nota = models.FloatField(
        verbose_name='Nota final',
        blank=True, null=True,
        default=avg_grade,
    )

    obs = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Observações')

    def __unicode__(self):
        return 'Redação nº %i: %s (%s)' \
               % (
                   self.id,
                   self.tema,
                   self.aluno,
               )

    class Meta:
        managed = True
        ordering = ('data_de_entrega',)
        verbose_name = 'Redação'
        verbose_name_plural = 'Redações'
