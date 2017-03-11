from django.contrib import admin
from politicas_afirmativas import models


class PedidoDeIsencaoUERJAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'get_parente', 'renda', 'has_cpf', 'has_rg', 'has_ctps', 'has_cr', ]
    list_filter = ('renda', 'has_cpf', 'has_rg', 'has_ctps', 'has_cr', )


class MembroDaFamiliaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'relacionamento', 'renda', 'has_cpf', 'has_rg', 'has_ctps', 'has_cr', ]
    list_filter = ('renda', 'has_cpf', 'has_rg', 'has_ctps', 'has_cr',)


class CodigoAdmin(admin.ModelAdmin):
    list_display = ['ano', 'cod', 'universidade', ]
    list_filter = ['ano', 'cod', 'universidade', ]


admin.site.register(models.PedidoDeIsencaoUERJ, PedidoDeIsencaoUERJAdmin)
admin.site.register(models.MembroDaFamilia, MembroDaFamiliaAdmin)
admin.site.register(models.Codigo, CodigoAdmin)
