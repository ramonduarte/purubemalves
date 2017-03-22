# coding=utf-8
from django.shortcuts import render, HttpResponse
from website import models as wm
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
