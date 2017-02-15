from django.contrib import admin
from projeto_redacao import models


class ProfessorDeRedacaoAdmin(admin.ModelAdmin):
    list_display = ['get_nome']
    # list_filter = ('voluntario',)


class TemaAdmin(admin.ModelAdmin):
    list_display = ['titulo', ]
    # list_filter = ('equipe', 'curso_pretendido', 'chegada', )


class RedacaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_aluno', 'get_corretor', 'data_de_entrega', 'data_de_correcao', 'is_devolvida']
    list_filter = ('corretor', 'aluno', 'is_devolvida')


admin.site.register(models.ProfessorDeRedacao, ProfessorDeRedacaoAdmin)
admin.site.register(models.Tema, TemaAdmin)
admin.site.register(models.Redacao, RedacaoAdmin)
