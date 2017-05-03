from django.contrib import admin
from home import models
from website import admin as wadmin
from django.utils.translation import ugettext as _


class PedidoDeInscricaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_do_pedido', ]
    list_filter = ['data_do_pedido', ]

    fieldsets = wadmin.AlunoAdmin.fieldsets

    def save_as_aluno(self, request):
        new_aluno = models.wm.Aluno(
            nome=self.nome,
            cpf=self.cpf,
            data_de_nascimento=self.data_de_nascimento,
            cep=self.cep,
            endereco=self.endereco,
            complemento=self.complemento,
            bairro=self.bairro,
            cidade=self.cidade,
            estado=self.estado,
            tel=self.tel,
            email=self.email,
            lingua_estrangeira=self.lingua_estrangeira,
            curso_pretendido=self.curso_pretendido,
            data_de_inscricao=self.data_de_inscricao,
            turma=self.turma,
            ano_letivo=self.ano_letivo,
        )
        new_aluno.save()

        print 'aaaaaaaaaaa'

        from django.http import HttpResponse
        return HttpResponse('aewwww')

    def extra_context(self):
        extra_buttons = [
            {
                'url': '_save_as_aluno',
                # 'textname': _('Matricular'),
                'func': self.save_as_aluno
            },
        ]
        return extra_buttons

    # from django.utils.safestring import mark_safe
    # extra_buttons = [
    #     mark_safe(
    #         '<input type="submit" value="Matricular" class="default" name="_save_as_aluno" />'
    #     ),
    #
    #     # {
    #     #     'url': 'huehuehue',
    #     #     'textname': _('Matricular'),
    #     #     'func': save_as_aluno
    #     # },
    # ]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or self.extra_context()
        # extra_context = extra_context or self.extra_buttons
        return super(PedidoDeInscricaoAdmin, self).change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    # Adds the custom button url
    def get_urls(self):
        from django.conf.urls import url
        urls = super(PedidoDeInscricaoAdmin, self).get_urls()
        my_urls = list(
            (url(r'^(.+)/%(url)s/$' % b, self.admin_site.admin_view(b['func'])) for b in self.extra_context())
        )
        return my_urls + urls


admin.site.register(models.PedidoDeInscricao, PedidoDeInscricaoAdmin)
