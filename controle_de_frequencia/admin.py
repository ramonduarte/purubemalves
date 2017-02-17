from django.contrib import admin
from controle_de_frequencia import models as cf


class ListaDePresencaDeVoluntariosAdmin(admin.ModelAdmin):
    list_filter = ('data',)
    list_display = ['get_voluntario', 'data', ]


class ListaDePresencaDeAlunosAdmin(admin.ModelAdmin):
    list_filter = ('data',)
    list_display = ['get_aluno', 'data', ]


admin.site.register(cf.ListaDePresencaDeVoluntarios, ListaDePresencaDeVoluntariosAdmin)
admin.site.register(cf.ListaDePresencaDeAlunos, ListaDePresencaDeAlunosAdmin)
