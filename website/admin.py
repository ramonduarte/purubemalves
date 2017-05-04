# coding=utf-8
from django.contrib import admin
from django.forms import ModelForm
from website import models, views


class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'get_nome',
        'turma',
        'get_attendance',
        'bairro',
        'cidade',
        'tel',
        'data_de_inscricao'
    ]
    list_filter = ('turma', 'is_ativo')
    search_fields = ('nome',)
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
                ('turma', 'ano_letivo', 'data_de_inscricao', ),
                ('lingua_estrangeira', 'curso_pretendido'),
                ('obs', 'is_ativo'),
            ),
        }),
    )

    formfield_overrides = {
        models.models.ManyToManyField: {
            'widget': views.autocomplete.ModelSelect2Multiple(url='curso-autocomplete'),
        }
    }

    class Media:
        js = (
            # 'django.jQuery',
            'admin/js/cep.js',
        )


class VoluntarioAdminForm(ModelForm):
    class Meta:
        model = models.Voluntario
        exclude = []
        widgets = {
            'graduacao': views.autocomplete.ModelSelect2Multiple(url='curso-autocomplete'),
            'equipe': views.autocomplete.ModelSelect2Multiple(url='equipe-autocomplete'),
        }


class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ['get_nome', 'get_equipe', 'get_attendance', 'tel', 'is_ativo', 'chegada', ]
    list_filter = ('equipe', 'is_ativo', )
    search_fields = ('nome',)

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
                ('equipe', 'chegada', ),
                ('graduacao', 'graduacao_concluida', ),
                ('is_ativo', ),
                ('obs', ),
            ),
        }),
    )

    form = VoluntarioAdminForm

    class Media:
        js = (
            # 'django.jQuery',
            'admin/js/cep.js',
        )


class CursoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'get_count',
        'uerj_peso_2',
        'uerj_peso_1',
        'cederj_especifica1',
        'cederj_especifica2',
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
class EditoraAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class AutorAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class LivroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'editora', 'isbn', 'is_disponivel', 'idioma', 'ano_de_publicacao', 'data_de_aquisicao', ]
    list_filter = ('is_disponivel', 'idioma')


class EmprestimoParaAlunoAdmin(admin.ModelAdmin):
    list_display = [
        'aluno',
        'get_turma',
        'livro',
        'emprestado_por',
        'data_de_emprestimo',
        'data_de_devolucao',
        'devolvido',
    ]
    list_filter = ('devolvido', 'aluno__turma', 'data_de_emprestimo', 'data_de_devolucao', )
    actions = ['set_as_devolvido']
    actions_on_bottom = True

    def set_as_devolvido(self, request, queryset):
        rows_updated = queryset.update(devolvido=True)
        if rows_updated == 1:
            message_bit = "O livro em questão foi marcado como devolvido."
        else:
            message_bit = "%s livros foram marcados como devolvidos." % rows_updated
        self.message_user(request, message_bit)
    set_as_devolvido.short_description = "Marcar livros selecionados como devolvidos"


class EmprestimoParaVoluntarioAdmin(admin.ModelAdmin):
    list_display = ['voluntario', 'livro', 'emprestado_por', 'data_de_emprestimo', 'data_de_devolucao', 'devolvido', ]
    list_filter = ('devolvido', 'data_de_emprestimo', 'data_de_devolucao',)
    actions = ['set_as_devolvido']
    actions_on_bottom = True

    def set_as_devolvido(self, request, queryset):
        rows_updated = queryset.update(devolvido=True)
        if rows_updated == 1:
            message_bit = "O livro em questão foi marcado como devolvido."
        else:
            message_bit = "%s livros foram marcados como devolvidos." % rows_updated
        self.message_user(request, message_bit)

    set_as_devolvido.short_description = "Marcar livros selecionados como devolvidos"


admin.site.register(models.Aluno, AlunoAdmin)
admin.site.register(models.Voluntario, VoluntarioAdmin)
admin.site.register(models.Curso, CursoAdmin)
admin.site.register(models.Equipe, EquipeAdmin)
admin.site.register(models.Ementa, EmentaAdmin)

# Library django-admin registering
admin.site.register(models.Livro, LivroAdmin)
admin.site.register(models.Editora, EditoraAdmin)
admin.site.register(models.Autor, AutorAdmin)
admin.site.register(models.EmprestimoParaAluno, EmprestimoParaAlunoAdmin)
admin.site.register(models.EmprestimoParaVoluntario, EmprestimoParaVoluntarioAdmin)
