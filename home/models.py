# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from website import models as wm


class PedidoDeInscricao(wm.Pessoa):
    lingua_estrangeira = models.CharField(
        default=u'Espanhol',
        max_length=wm.supershortfield,
        verbose_name='Língua Estrangeira',
        choices=[
            (u'Espanhol', u'Espanhol'),
            (u'Inglês', u'Inglês'),
            (u'Francês', u'Francês (obs: não possuímos professor no momento)'),
        ])
    curso_pretendido = models.ManyToManyField(wm.Curso, blank=True, verbose_name='Curso Pretendido')

    # excluded from the form visible to candidates
    data_do_pedido = models.DateField(default=wm.date.today, verbose_name=u'Data do Pedido')
    data_de_inscricao = models.DateField(default=wm.date.today, verbose_name=u'Data de Inscrição')
    turma = models.CharField(max_length=1, blank=True, null=True, choices=(
        (u'A', u'A'),
        (u'B', u'B'),
        (u'C', u'C'),
        (u'D', u'D'),
        (u'F', u'F'),
    ), default=u'A')
    obs = models.CharField(max_length=200, blank=True, null=True, verbose_name='Observações')
    ano_letivo = models.IntegerField(default=2017, verbose_name='Ano letivo')

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)
        verbose_name = u'Pedido de Inscrição'
        verbose_name_plural = u'Pedidos de Inscrição'
