# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from website import models as wm
import datetime


# def avg_grade():
#     return 500  # TODO: return average of competencias (2017/02/15)


class ProfessorDeRedacao(models.Model):
    voluntario = models.ForeignKey(wm.Voluntario)

    def get_nome(self):
        return self.voluntario.nome
        # return wm.Voluntario.objects.get(pk=self.voluntario_id).nome
    get_nome.short_description = 'Nome'

    def get_equipe(self):
        return [self.voluntario.equipe.all()[i] for i in range(len(self.voluntario.equipe.all()))]
    get_equipe.short_description = 'Equipe'

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
    aluno = models.ForeignKey(wm.Aluno)

    def get_corretor(self):
        return [self.corretor.all()[i] for i in range(len(self.corretor.all()))]
    get_corretor.short_description = 'Corretores'

    def get_aluno(self):
        return self.aluno.nome
    get_aluno.short_description = 'Aluno'

    def get_turma(self):
        return self.aluno.turma
    get_turma.short_description = 'Turma'

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

    # 2017/03/15: All descriptions provided by Luiz Henrique Davi de Lemos.
    # 2017/03/15: 1 - Norma Padrão da Língua: Demonstrar domínio da norma culta da língua escrita.
    competencia1 = models.FloatField(
        verbose_name='Norma padrão da língua',
        blank=True, null=True,
    )
    # 2017/03/15: 2 - Compreensão do tema: Compreender a proposta de redação e aplicar conceitos das
    # várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais
    # do texto dissertativo-argumentativo.
    competencia2 = models.FloatField(
        verbose_name='Compreensão do tema',
        blank=True, null=True,
    )
    # 2017/03/15: 3 - Coerência: Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões
    # e argumentos em defesa de um ponto de vista.
    competencia3 = models.FloatField(
        verbose_name='Coerência',
        blank=True, null=True,
    )
    # 2017/03/15: 4 - Coesão: Demonstrar conhecimento dos mecanismos linguísticos necessários para
    # a construção da argumentação.
    competencia4 = models.FloatField(
        verbose_name='Coesão',
        blank=True, null=True,
    )
    # 2017/03/15: 5 - Proposta de intervenção: Elaborar proposta de solução para o problema abordado,
    # mostrando respeito aos valores humanos e considerando a diversidade sociocultural.
    competencia5 = models.FloatField(
        verbose_name='Proposta de intervenção',
        blank=True, null=True,
    )

    nota = models.FloatField(
        verbose_name='Nota final',
        blank=True, null=True,
    )

    obs = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Observações')

    def __unicode__(self):
        return 'Redação nº %i: %s (%s - turma %s)' \
               % (
                   self.id,
                   self.tema,
                   self.aluno,
                   self.get_turma(),
               )

    class Meta:
        managed = True
        ordering = ('id',)
        verbose_name = 'Redação'
        verbose_name_plural = 'Redações'
