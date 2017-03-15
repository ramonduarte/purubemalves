# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from website import models as wm
from datetime import date, timedelta


class PedidoDePoliticaAfirmativa(models.Model):
    aluno = models.ForeignKey(wm.Aluno, on_delete=models.CASCADE)
    membros = models.ManyToManyField('MembroDaFamilia', verbose_name=u'Parente')

    rg = models.CharField(max_length=wm.supershortfield, blank=True, null=True, verbose_name=u'RG')
    emissor_rg = models.CharField(max_length=wm.supershortfield, blank=True, null=True, verbose_name=u'Órgão Emissor')
    data_rg = models.DateField(blank=True, null=True, verbose_name=u'Data de emissão')

    renda = models.IntegerField()

    status_em = models.CharField(max_length=wm.supershortfield, verbose_name=u'Ensino médio', choices=(
        (u'Concluinte', u'Concluinte em 2017'),
        (u'Concluído', u'Concluído'),
        (u'Outro', u'Outro'),
    ), default=u'Concluinte')

    certificado = models.FileField(blank=True, null=True, upload_to='',
                                   verbose_name=u'Certificado de conclusão do Ensino Médio')
    copia_cpf = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia do CPF')
    copia_rg = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia do RG')
    copia_ctps = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia da CTPS')
    copia_cr = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia da CR')
    copia_residencia = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Comprovante de residência')

    typeof_rg = models.CharField(max_length=wm.supershortfield, blank=True, null=True, choices=(
        (u'ID civil', u'Identidade civil'),
        (u'ID militar', u'Identidade militar'),
        (u'CNH', u'Carteira de motorista'),
        (u'CHP', u'Carteira de habilitação profissional'),
        (u'Outro', u'Outro'),
    ), verbose_name=u'Tipo de identidade')
    typeof_cr = models.CharField(max_length=wm.supershortfield, blank=True, null=True, choices=(
        (u'Contracheque', u'Contracheque'),
        (u'Recibo de benefício social', u'Recibo de benefício social'),
        (u'Declaração de próprio punho', u'Declaração de próprio punho'),
        (u'Outra', u'Outra'),
    ), verbose_name=u'Tipo de comprovação de renda')
    typeof_renda = models.CharField(max_length=wm.supershortfield, blank=True, null=True, choices=(
        (u'Carteira assinada', u'Trabalho com carteira assinada'),
        (u'Informal', u'Trabalho sem carteira assinada'),
        (u'Autônomo', u'Trabalho autônomo ou profissional liberal'),
        (u'Benefício social', u'Benefício social'),
        (u'Bolsa', u'Bolsa de estágio ou iniciação'),
        (u'INSS', u'Aposentadoria do INSS'),
        (u'Previdência privada', u'Aposentadoria ou previdência privada'),
        (u'Outra', u'Outra'),
    ), verbose_name=u'Tipo de fonte de renda')
    typeof_residencia = models.CharField(max_length=wm.supershortfield, blank=True, null=True, choices=(
        (u'Luz', u'Luz'),
        (u'Água', u'Água'),
        (u'Gás', u'Gás'),
        (u'Telefone', u'Telefone fixo ou internet fixa'),
        (u'Celular', u'Telefone celular ou internet móvel'),
        (u'TV por assinatura', u'TV'),
        (u'Cartão de crédito', u'Cartão de Crédito'),
        (u'Outra', u'Outra'),
    ), verbose_name=u'Tipo de comprovante de residência')

    has_cpf = models.BooleanField(default=False, verbose_name=u'CPF entregue')
    has_rg = models.BooleanField(default=False, verbose_name=u'RG entregue')
    has_ctps = models.BooleanField(default=False, verbose_name=u'CTPS entregue')
    has_cr = models.BooleanField(default=False, verbose_name=u'Comprovação de renda')

    obs = models.CharField(max_length=wm.superlongfield, blank=True, null=True, verbose_name=u'Observações')

    def __unicode__(self):
        return '%s' % (self.aluno,)

    def get_parente(self):
        return [self.membros.all()[i] for i in range(len(self.membros.all()))]
    get_parente.verbose_name = u'Parentes'

    class Meta:
        managed = True
        abstract = True
        verbose_name = u'Pedido de Política Afirmativa'
        verbose_name_plural = u'Pedido de Política Afirmativa'


class PedidoDeIsencaoUERJ(PedidoDePoliticaAfirmativa):
    codigo = models.ForeignKey('Codigo', verbose_name=u'Código UERJ')
    exame = models.CharField(max_length=wm.supershortfield, verbose_name=u'Exame', choices=(
        (u'EQ1', '1º Exame de Qualificação'),
        (u'EQ2', '2º Exame de Qualificação'),
    ))
    concurso = models.IntegerField(default=2018, verbose_name=u'Ano do concurso')
    data_de_submissao = models.DateField(default=date.today, verbose_name=u'Data de submissão')
    data_de_entrega = models.DateField(blank=True, null=True, verbose_name=u'Data de entrega')
    resposta = models.NullBooleanField(blank=True, null=True, verbose_name=u'Aprovado')

    class Meta:
        managed = True
        verbose_name = u'Isenção de Inscrição UERJ'
        verbose_name_plural = u'Isenções de Inscrição UERJ'


class MembroDaFamilia(wm.Pessoa):
    relacionamento = models.CharField(max_length=wm.supershortfield, verbose_name=u'Relacionamento')

    rg = models.CharField(max_length=wm.supershortfield, blank=True, null=True, verbose_name=u'RG')
    emissor_rg = models.CharField(max_length=wm.supershortfield, blank=True, null=True, verbose_name=u'Órgão Emissor')
    data_rg = models.DateField(blank=True, null=True, verbose_name=u'Data de emissão')

    renda = models.IntegerField(verbose_name=u'Renda')

    copia_cpf = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia do CPF')
    copia_rg = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia do RG')
    copia_ctps = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia da CTPS')
    copia_cr = models.FileField(blank=True, null=True, upload_to='', verbose_name=u'Cópia da CR')

    typeof_rg = models.CharField(max_length=wm.supershortfield, blank=True, null=True, choices=(
        (u'Identidade civil', u'ID civil'),
        (u'Identidade militar', u'ID militar'),
        (u'Carteira de motorista', u'CNH'),
        (u'Carteira de habilitação profissional', u'CHP'),
        (u'Outro', u'Outro'),
    ), verbose_name=u'Tipo de comprovação de renda')
    typeof_cr = models.CharField(max_length=wm.supershortfield, blank=True, null=True, choices=(
        (u'Contracheque', u'Contracheque'),
        (u'Recibo de benefício social', u'Recibo de benefício social'),
        (u'Declaração de próprio punho', u'Declaração de próprio punho'),
        (u'Outra', u'Outra'),
    ), verbose_name=u'Tipo de comprovação de renda')
    typeof_renda = models.CharField(max_length=wm.supershortfield, blank=True, null=True, choices=(
        (u'Trabalho com carteira assinada', u'Carteira assinada'),
        (u'Trabalho sem carteira assinada', u'Informal'),
        (u'Trabalho autônomo ou profissional liberal', u'Autônomo'),
        (u'Benefício social', u'Benefício social'),
        (u'Bolsa de estágio ou iniciação', u'Bolsa'),
        (u'Aposentadoria do INSS', u'INSS'),
        (u'Aposentadoria ou previdência privada', u'Previdência privada'),
        (u'Outra', u'Outra'),
    ), verbose_name=u'Tipo de fonte de renda')

    has_cpf = models.BooleanField(default=False, verbose_name=u'CPF entregue')
    has_rg = models.BooleanField(default=False, verbose_name=u'RG entregue')
    has_ctps = models.BooleanField(default=False, verbose_name=u'CTPS entregue')
    has_cr = models.BooleanField(default=False, verbose_name=u'Comprovação de renda')

    def __unicode__(self):
        return '%s (%s)' % (self.nome, self.relacionamento)

    class Meta:
        managed = True
        verbose_name = u'Membro da família'
        verbose_name_plural = u'Membros da família'


class Codigo(models.Model):
    ano = models.IntegerField(default=2018, verbose_name=u'Ano do concurso')
    cod = models.CharField(max_length=wm.supershortfield, verbose_name=u'Código')
    universidade = models.CharField(max_length=wm.supershortfield, verbose_name=u'Instituição', choices=(
        (u'UERJ', u'UERJ'),
        (u'UFRJ', u'UFRJ'),
        (u'UFF', u'UFF'),
        (u'CEDERJ', u'CEDERJ'),
    ))

    def __unicode__(self):
        return '%s (%s)' % (self.cod, self.universidade)

    class Meta:
        managed = True
        verbose_name = u'Código'
        verbose_name_plural = u'Códigos'
