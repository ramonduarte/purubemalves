# coding=utf-8
from django.shortcuts import render, HttpResponse
from website import models as wm
from dal import autocomplete
import requests


def getcep(request):
    if request.method == 'GET':
        cep = request.GET[u'cep']
        r = requests.get(
            "http://cep.republicavirtual.com.br/web_cep.php",
            params={'cep': cep, 'formato': 'json'},
        ).content
        return HttpResponse(r)
    else:
        return render(request, 'common/404.html')


class CursoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return wm.Curso.objects.none()

        qs = wm.Curso.objects.all()

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)

        return qs


class EquipeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return wm.Equipe.objects.none()

        qs = wm.Equipe.objects.all()

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)

        return qs


class AutorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return wm.Autor.objects.none()

        qs = wm.Autor.objects.all()

        if self.q:
            qs = qs.filter(nome__istartswith=self.q)

        return qs
