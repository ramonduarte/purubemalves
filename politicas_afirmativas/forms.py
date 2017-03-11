# -*- coding: utf-8 -*-
from django import forms
from politicas_afirmativas import models as pam
from django.utils.translation import ugettext_lazy as _


class PedidoForm(forms.ModelForm):

    class Meta:
        model = pam.PedidoDeIsencaoUERJ
        exclude = (
            'obs',
        )
