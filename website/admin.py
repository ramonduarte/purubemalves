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
                ('tel', 'email'),
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

    list_display = ['get_nome', 'turma', 'bairro', 'cidade', 'tel', 'data_de_inscricao']
    list_filter = ('turma',)

    # list_filter = ('turma', 'bairro', 'cidade', 'lingua_estrangeira', 'curso_pretendido', 'ano_letivo', )

    class Media:
        js = (
            # 'django.jQuery',
            'admin/js/cep.js',
        )


class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['get_nome', 'get_equipe', 'tel', 'is_ativo', 'chegada', ]
    list_filter = ('equipe', 'is_ativo', )

    fieldsets = (
        ('Informações Pessoais', {
            'fields': (
                ('nome', 'cpf', 'data_de_nascimento'),
                ('cep', 'endereco', 'complemento'),
                ('bairro', 'cidade', 'estado'),
                ('tel', 'email'),
            ),
        }),
        ('Informações Profissionais', {
            'fields': (
                ('equipe', ),
                ('graduacao', 'graduacao_concluida', ),
                ('is_ativo', ),
                ('obs', 'chegada'),
            ),
        }),
    )

    class Media:
        js = (
            # 'django.jQuery',
            'admin/js/cep.js',
        )


# class TelefoneAdmin(admin.ModelAdmin):
#     list_display = ['num', ]
#     # list_filter =


class CursoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'get_count',
        'uerj_peso_2',
        'uerj_peso_1',
        'ufrj_mat_peso',
        'ufrj_lin_peso',
        'ufrj_nat_peso',
        'ufrj_hum_peso',
        'ufrj_red_peso',
    ]
    list_filter = ('uerj_peso_2', 'uerj_peso_1', )


class EmentaAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'data', 'ano_letivo']
    list_filter = ('disciplina', 'ano_letivo',)


class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_count', 'is_gestao', 'gerente', ]
    list_filter = ('is_gestao',)


# Library classes
class LivroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'editora', 'isbn', 'is_disponivel', 'idioma', 'ano_de_publicacao', 'data_de_aquisicao', ]
    list_filter = ('is_disponivel', 'idioma')


class EditoraAdmin(admin.ModelAdmin):
    list_display = ['nome']
    list_filter = ('nome',)


class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', ]
    # list_filter = ('sobrenome', )


class EmprestimoParaAlunoAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'get_turma', 'livro', 'emprestado_por', 'data_de_emprestimo', 'data_de_devolucao', 'devolvido', ]
    list_filter = ('devolvido', 'aluno__turma', 'data_de_emprestimo', 'data_de_devolucao', )


class EmprestimoParaVoluntarioAdmin(admin.ModelAdmin):
    list_display = ['voluntario', 'livro', 'emprestado_por', 'data_de_emprestimo', 'data_de_devolucao', 'devolvido', ]
    list_filter = ('devolvido', 'data_de_emprestimo', 'data_de_devolucao',)


admin.site.register(models.Aluno, AlunoAdmin)
admin.site.register(models.Voluntario, VoluntarioAdmin)
# admin.site.register(models.Telefone, TelefoneAdmin)
admin.site.register(models.Curso, CursoAdmin)
admin.site.register(models.Equipe, EquipeAdmin)
admin.site.register(models.Ementa, EmentaAdmin)

# Library django-admin registering
admin.site.register(models.Livro, LivroAdmin)
admin.site.register(models.Editora, EditoraAdmin)
admin.site.register(models.Autor, AutorAdmin)
admin.site.register(models.EmprestimoParaAluno, EmprestimoParaAlunoAdmin)
admin.site.register(models.EmprestimoParaVoluntario, EmprestimoParaVoluntarioAdmin)
