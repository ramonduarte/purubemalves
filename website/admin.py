# coding=utf-8
from django.contrib import admin
from website import models


class AlunoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informações Pessoais', {
            'fields': (
                ('nome', 'cpf', 'data_de_nascimento'),
                ('cep', 'endereco', 'complemento'),
                ('bairro', 'cidade', 'estado'),
                # ('tel', 'telefone'),  # TODO: deprecate this line (2017/03/07)
                ('tel', 'email'),  # TODO: enable this line (2017/03/07)
                # 'email',  # TODO: deprecate this line (2017/03/07)
            ),
        }),
        ('Informações Letivas', {
            'fields': (
                ('turma', 'ano_letivo'),
                ('lingua_estrangeira', 'curso_pretendido'),
                ('obs', 'data_de_inscricao'),
            ),
        }),
    )
    # fields = (
    #     ('nome', 'cpf', 'data_de_nascimento'),
    #     ('endereco', 'complemento', 'cep'),
    #     ('bairro', 'cidade', 'estado'),
    #     ('tel', 'telefone'),  # TODO: deprecate this line (2017/03/07)
    #     # ('tel', 'email'),   TODO: enable this line (2017/03/07)
    #     'email',
    #     ('turma', 'ano_letivo'),
    #     'lingua_estrangeira',
    #     'curso_pretendido',
    #     'obs',
    # )
    list_filter = ('turma',)
    list_display = ['get_nome', 'turma', 'bairro', 'cidade', 'tel']

    # list_filter = ('turma', 'bairro', 'cidade', 'lingua_estrangeira', 'curso_pretendido', 'ano_letivo', )

    class Media:
        js = (
            # 'django.jQuery',
            'admin/js/cep.js',
        )


class VoluntarioAdmin(admin.ModelAdmin):
    list_filter = ('equipe', 'is_ativo')
    list_display = ['get_nome', 'tel', 'is_ativo']
    # list_filter = ('equipe', 'curso_pretendido', 'chegada', )


# class TelefoneAdmin(admin.ModelAdmin):
#     list_display = ['num', ]
#     # list_filter =


class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uerj_peso_1', 'uerj_peso_2', ]
    list_filter = ('uerj_peso_1', 'uerj_peso_2',)


class EmentaAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'data', 'ano_letivo']
    list_filter = ('disciplina', 'ano_letivo',)


class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'is_gestao', 'gerente', ]
    list_filter = ('is_gestao',)


# Library classes
class LivroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'editora', 'isbn', 'is_disponivel', 'ano_de_publicacao', 'data_de_aquisicao', ]
    list_filter = ('is_disponivel',)


class EditoraAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ('nome',)


class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', ]
    # list_filter = ('sobrenome', )


class EmprestimoParaAlunoAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'livro', 'emprestado_por', 'data_de_emprestimo', 'data_de_devolucao', 'devolvido', ]
    list_filter = ('devolvido', 'data_de_emprestimo', 'data_de_devolucao', )


class EmprestimoParaVoluntarioAdmin(admin.ModelAdmin):
    list_display = ['voluntario', 'livro', 'emprestado_por', 'data_de_emprestimo', 'data_de_devolucao', 'devolvido', ]
    list_filter = ('devolvido', 'data_de_emprestimo', 'data_de_devolucao',)


admin.site.register(models.Aluno, AlunoAdmin)
admin.site.register(models.Voluntario, VoluntarioAdmin)
# admin.site.register(models.Telefone, TelefoneAdmin)
admin.site.register(models.Curso, CursoAdmin)
admin.site.register(models.Equipe, EquipeAdmin)
admin.site.register(models.Ementa, EmentaAdmin)

# Library adjango-admin registering
admin.site.register(models.Livro, LivroAdmin)
admin.site.register(models.Editora, EditoraAdmin)
admin.site.register(models.Autor, AutorAdmin)
admin.site.register(models.EmprestimoParaAluno, EmprestimoParaAlunoAdmin)
admin.site.register(models.EmprestimoParaVoluntario, EmprestimoParaVoluntarioAdmin)
