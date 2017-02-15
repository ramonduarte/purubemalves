# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from datetime import date, timedelta
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
    """
    TODO: Write a description for this model (2017/01/31)
    """
    num = models.CharField(max_length=shortfield, verbose_name='Número')

    def __unicode__(self):
        return '%s' % (self.num.replace(' ', ''),)

    class Meta:
        managed = True
        ordering = ('num',)


class Curso(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    nome = models.CharField(max_length=longfield)
    uerj_peso_1 = models.CharField(max_length=shortfield, blank=True, null=True, verbose_name='UERJ Peso 1')
    uerj_peso_2 = models.CharField(max_length=shortfield, blank=True, null=True, verbose_name='UERJ Peso 2')
    ufrj_mat_peso = models.IntegerField(blank=True, null=True, verbose_name='UFRJ Peso Matemática')
    ufrj_lin_peso = models.IntegerField(blank=True, null=True, verbose_name='UFRJ Peso Linguagens')
    ufrj_nat_peso = models.IntegerField(blank=True, null=True, verbose_name='UFRJ Peso Natureza')
    ufrj_hum_peso = models.IntegerField(blank=True, null=True, verbose_name='UFRJ Peso Humanidades')
    ufrj_red_peso = models.IntegerField(blank=True, null=True, verbose_name='UFRJ Peso Redação')

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)


class Pessoa(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    nome = models.CharField(max_length=longfield)
    cpf = models.BigIntegerField(verbose_name='CPF')
    data_de_nascimento = models.DateField(verbose_name='Data de Nascimento')
    endereco = models.CharField(max_length=longfield, verbose_name='Endereço')
    complemento = models.CharField(max_length=shortfield, blank=True, null=True)
    bairro = models.CharField(max_length=shortfield)
    cep = models.IntegerField(verbose_name='CEP')
    cidade = models.CharField(max_length=shortfield)
    estado = models.CharField(max_length=2, choices=br_states.STATE_CHOICES)
    telefone = models.ManyToManyField(Telefone)  # a person can have several phone numbers
    email = models.EmailField(blank=True, null=True)
    foto = models.CharField(max_length=longfield, blank=True, null=True)
    facebook = models.CharField(max_length=longfield, blank=True, null=True)
    twitter = models.CharField(max_length=longfield, blank=True, null=True)
    site = models.CharField(max_length=longfield, blank=True, null=True)
    blog = models.CharField(max_length=longfield, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.nome,)

    def get_endereco(self):
        return self.endereco + ', ' + self.complemento + ', ' + self.bairro + ', ' + self.cidade

    def get_contatos(self):
        return 'Telefone: %s\nE-mail: %s\nFacebook: %s' % (self.telefone, self.email, self.facebook)

    class Meta:
        managed = True
        ordering = ('nome',)
        abstract = True


class Aluno(Pessoa):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    turma = models.CharField(max_length=1, blank=True, null=True)
    lingua_estrangeira = models.CharField(default=u'Espanhol', max_length=supershortfield,
                                          verbose_name='Língua Estrangeira', choices=[
                                              (u'Espanhol', u'Espanhol'),
                                              (u'Inglês', u'Inglês'),
                                              (u'Francês', u'Francês (obs: não possuímos professor no momento)'),
                                            ])
    # curso_pretendido = models.CharField(blank=True, null=True, max_length=30)
    curso_pretendido = models.ManyToManyField(Curso, blank=True, verbose_name='Curso Pretendido')
    obs = models.CharField(max_length=200, blank=True, null=True, verbose_name='Observações')
    ano_letivo = models.IntegerField(default=2017, verbose_name='Ano letivo')

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)


class Voluntario(Pessoa):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    equipe = models.ManyToManyField('Equipe')
    graduacao = models.OneToOneField(Curso, blank=True, null=True, verbose_name='Graduação')
    graduacao_concluida = models.BooleanField(default=False, verbose_name='Concluída')
    obs = models.CharField(max_length=superlongfield, blank=True, null=True, verbose_name='Observações')
    chegada = models.DateField(blank=True, null=True)
    is_ativo = models.BooleanField(default=True, verbose_name='Ativo')

    # def get_equipe(self):  # TODO: Fix MaxRecursionError (2017/02/15)
    #     return [self.equipe.all()[i] for i in range(len(self.equipe.all()))]

    def __unicode__(self):
        return '%s' % (self.nome,)
        # return '%s (%s)' % (self.nome, self.get_equipe) # TODO: Decomment when get_equipe() gets fixed

    class Meta:
        managed = True
        ordering = ('nome',)
        verbose_name = 'Voluntário'
        verbose_name_plural = 'Voluntários'


class Equipe(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    nome = models.CharField(max_length=30)
    is_gestao = models.BooleanField(default=False, verbose_name='Gestão')
    gerente = models.ForeignKey('Voluntario', blank=True, null=True,
                                related_name='gerente')  # workaround to pass makemigrations

    def __unicode__(self):
        return '%s' % (self.nome,)

    class Meta:
        managed = True
        ordering = ('nome',)


class Ementa(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    disciplina = models.ForeignKey(Equipe)
    data = models.DateField(blank=True, null=True)
    ano_letivo = models.IntegerField(default=2017, verbose_name='Ano letivo')
    obs = models.CharField(max_length=superlongfield, blank=True, null=True, verbose_name='Observações')

    def __unicode__(self):
        return 'Ementa da disciplina de %s para o ano letivo de %s' % (self.disciplina, self.ano_letivo)

    class Meta:
        managed = True
        ordering = ('disciplina',)


class Livro(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    nome = models.CharField(max_length=superlongfield)
    isbn = models.CharField(max_length=13, verbose_name='ISBN', blank=True, null=True)
    editora = models.ForeignKey('Editora')
    autor = models.ManyToManyField('Autor')
    ano_de_publicacao = models.CharField(max_length=4, verbose_name='Ano de Publicação', blank=True, null=True)
    data_de_aquisicao = models.DateField(default=date.today, verbose_name='Data de Aquisição')
    is_disponivel = models.BooleanField(default=True, verbose_name='Disponível')

    def lend(self):
        self.is_disponivel = False

    def giveback(self):
        self.is_disponivel = True

    def get_editora(self):
        return Editora.objects.get(pk=self.editora_id).nome

    def __unicode__(self):
        return 'Livro: ' + self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = "Livro"
        verbose_name_plural = "Livros"


class Editora(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    nome = models.CharField(max_length=longfield)

    def __unicode__(self):
        return '%s' % self.nome

    class Meta:
        get_latest_by = "nome"
        ordering = ['nome']


class Autor(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    nome = models.CharField(max_length=longfield)
    sobrenome = models.CharField(max_length=longfield)

    def __unicode__(self):
        return 'Autor: ' + self.nome + ' ' + self.sobrenome

    class Meta:
        get_latest_by = "name"
        ordering = ['nome', 'sobrenome']
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


# Function to overcome Django runtime limitations
def default_timedelta():
    return date.today() + timedelta(+14)


class Emprestimo(models.Model):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    livro = models.ForeignKey(Livro)
    emprestado_por = models.ForeignKey(Voluntario, null=True, blank=True, related_name='%(class)s_related')
    data_de_emprestimo = models.DateField(default=date.today, verbose_name='Empréstimo')
    data_de_devolucao = models.DateField(default=default_timedelta, verbose_name='Devolução')

    @classmethod
    def create(cls, livro):
        emprestimo = cls(livro=livro)
        livro.lend()
        return emprestimo

    def __unicode__(self):
        return 'Empréstimo: ' + unicode(self.data_de_emprestimo)

    class Meta:
        get_latest_by = "livro"
        ordering = ['data_de_emprestimo', 'livro']
        abstract = True


class EmprestimoParaAluno(Emprestimo):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    aluno = models.ForeignKey(Aluno, null=True, blank=True)

    class Meta:
        verbose_name = "Empréstimo para Alunos"
        verbose_name_plural = "Empréstimos para Alunos"


class EmprestimoParaVoluntario(Emprestimo):
    """
    TODO: Write a description for this model (2017/01/31)
    """
    voluntario = models.ForeignKey(Voluntario, null=True, blank=True, verbose_name='Voluntário')

    class Meta:
        verbose_name = "Empréstimo para Voluntários"
        verbose_name_plural = "Empréstimos para Voluntários"
