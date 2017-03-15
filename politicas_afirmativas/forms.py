# -*- coding: utf-8 -*-
from django import forms
from politicas_afirmativas import models as pam
from django.utils.translation import ugettext_lazy as _


class PedidoForm(forms.ModelForm):

    class Meta:
        model = pam.PedidoDeIsencaoUERJ
        exclude = (
            'aluno',
            'obs',
            'telefone',
            'email',
            'foto',
            'facebook',
            'twitter',
            'site',
            'blog',
        )
        # fields = (
        #     ('rg', 'emissor_rg', 'data_rg', 'typeof_rg', 'copia_rg', ),
        #     ('aluno.cpf', 'emissor_rg', 'data_rg', 'typeof_rg', 'copia_rg', ),
        #     ('status_em', 'certificado', ),
        #     ('status_em', 'certificado', ),
        # )
