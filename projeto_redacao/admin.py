# coding=utf-8
from django.contrib import admin
from projeto_redacao import models


class ProfessorDeRedacaoAdmin(admin.ModelAdmin):
    list_display = ['get_nome']
    # list_filter = ('voluntario',)


class TemaAdmin(admin.ModelAdmin):
    list_display = ['titulo', ]
    # list_filter = ('equipe', 'curso_pretendido', 'chegada', )


class RedacaoAdmin(admin.ModelAdmin):
    list_display = [
        'get_aluno', 'get_turma', 'get_corretor', 'data_de_entrega', 'data_de_correcao', 'is_devolvida'
    ]
    list_filter = ('corretor', 'is_devolvida')
    actions = ['set_as_devolvida']
    actions_on_bottom = True

    def set_as_devolvida(self, request, queryset):
        rows_updated = queryset.update(is_devolvida=True)
        if rows_updated == 1:
            message_bit = "A redação foi marcada como devolvida."
        else:
            message_bit = "%s redações foram marcadas como devolvidas." % rows_updated
        self.message_user(request, message_bit)

    set_as_devolvida.short_description = "Marcar redações selecionadas como devolvidas"

    class Media:
        js = (
            'admin/js/redacao.js',
        )


admin.site.register(models.ProfessorDeRedacao, ProfessorDeRedacaoAdmin)
admin.site.register(models.Tema, TemaAdmin)
admin.site.register(models.Redacao, RedacaoAdmin)
