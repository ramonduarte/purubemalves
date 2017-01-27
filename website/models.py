# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import date
from localflavor.br import br_states
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# Some predefinitions for most common fields
supershortfield = 10
shortfield = 30
longfield = 100
superlongfield = 200


class Telefone(models.Model):
    num = models.CharField(max_length=shortfield)

    def __unicode__(self):
        return '%s' % (self.num.replace(' ', ''),)

    class Meta:
        managed = True
        ordering = ('num',)


class Curso(models.Model):
    nome = models.CharField(max_length=longfield)
    uerj_peso_1 = models.CharField(max_length=shortfield, blank=True, null=True)
    uerj_peso_2 = models.CharField(max_length=shortfield, blank=True, null=True)
    ufrj_mat_peso = models.IntegerField()
    ufrj_lin_peso = models.IntegerField()
    ufrj_nat_peso = models.IntegerField()
    ufrj_hum_peso = models.IntegerField()
    ufrj_red_peso = models.IntegerField()

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)


class Pessoa(models.Model):
    nome = models.CharField(max_length=longfield)
    cpf = models.IntegerField()
    data_de_nascimento = models.DateField()
    endereco = models.CharField(max_length=longfield)
    complemento = models.CharField(max_length=shortfield, blank=True, null=True)
    bairro = models.CharField(max_length=shortfield)
    cep = models.IntegerField()
    cidade = models.CharField(max_length=shortfield)
    estado = models.CharField(max_length=2, choices=br_states.STATE_CHOICES)
    telefone = models.ManyToManyField(Telefone)  # a student can have several phone numbers
    email = models.EmailField(blank=True, null=True)
    foto = models.CharField(max_length=longfield, blank=True, null=True)
    facebook = models.CharField(max_length=longfield, blank=True, null=True)
    twitter = models.CharField(max_length=longfield, blank=True, null=True)
    site = models.CharField(max_length=longfield, blank=True, null=True)
    blog = models.CharField(max_length=longfield, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)
        abstract = True


class Aluno(Pessoa):
    turma = models.CharField(max_length=1, blank=True, null=True)
    lingua_estrangeira = models.CharField(default=u'Espanhol', max_length=supershortfield, choices=[
        (u'Espanhol', u'Espanhol'),
        (u'Inglês', u'Inglês'),
        (u'Francês', u'Francês (obs: não possuímos professor no momento)'),
    ])
    # curso_pretendido = models.CharField(blank=True, null=True, max_length=30)
    curso_pretendido = models.OneToOneField(Curso, blank=True, null=True)
    obs = models.CharField(max_length=200, blank=True, null=True)
    ano_letivo = models.DateField(default=date.today().year)

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)


class Voluntario(Pessoa):
    equipe = models.ManyToManyField('Equipe')
    graduacao = models.OneToOneField(Curso, blank=True, null=True)
    graduacao_concluida = models.BooleanField(default=False)
    obs = models.CharField(max_length=superlongfield, blank=True, null=True)
    chegada = models.DateField(default=date.today)

    def __unicode__(self):
        return '%s (%s)' % (self.nome, self.equipe)

    class Meta:
        managed = True
        ordering = ('nome',)


class Equipe(models.Model):
    nome = models.CharField(max_length=30)
    is_gestao = models.BooleanField(default=False)
    gerente = models.ForeignKey('Voluntario', blank=True, null=True,
                                related_name='gerente')  # workaround to pass makemigrations

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)


class Ementa(models.Model):
    disciplina = models.ForeignKey(Equipe)
    data = models.DateField(default=date.today)
    ano_letivo = models.DateField(default=date.today().year)
    obs = models.CharField(max_length=superlongfield, blank=True, null=True)

    def __unicode__(self):
        return 'Ementa da disciplina de %s para o ano letivo de %s' % (self.disciplina, self.ano_letivo)

    class Meta:
        managed = True
        ordering = ('disciplina',)
