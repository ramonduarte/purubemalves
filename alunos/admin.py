from django.contrib import admin
from alunos import models as am


class PerfilDeAlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'aluno', ]
    # list_filter = ()


admin.site.register(am.PerfilDeAluno, PerfilDeAlunoAdmin)
