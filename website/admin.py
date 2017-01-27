from django.contrib import admin
from website import models


# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_filter = ('turma',)
    # list_display =
    # list_filter = ('turma', 'bairro', 'cidade', 'lingua_estrangeira', 'curso_pretendido', 'ano_letivo', )


class VoluntarioAdmin(admin.ModelAdmin):
    list_filter = ('equipe',)
    # list_display =
    # list_filter = ('equipe', 'curso_pretendido', 'chegada', )


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ['num', ]
    # list_filter =


class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uerj_peso_1', 'uerj_peso_2', ]
    list_filter = ('uerj_peso_1', 'uerj_peso_2', )


class EmentaAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'data', 'ano_letivo']
    list_filter = ('disciplina', 'ano_letivo', )


class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'is_gestao', 'gerente', ]
    list_filter = ('is_gestao', )


admin.site.register(models.Aluno, AlunoAdmin)
admin.site.register(models.Voluntario, VoluntarioAdmin)
admin.site.register(models.Telefone, TelefoneAdmin)
admin.site.register(models.Curso, CursoAdmin)
admin.site.register(models.Equipe, EquipeAdmin)
admin.site.register(models.Ementa, EmentaAdmin)
