from django.shortcuts import render
from politicas_afirmativas import models as pam
from politicas_afirmativas import forms as paf
from website import models as wm


def index(request):
    if request.method == 'GET':
        html_variables = {

        }
        return render(request, 'politicas_afirmativas/index.html', html_variables)
    else:
        return render(request, 'common/404.html')


def uerj1(request):
    if request.method == 'GET':
        try:
            aluno = wm.Aluno.objects.get(cpf=request.GET['id_cpf'][0])
            pedido = paf.PedidoForm(instance=aluno)
        except wm.Aluno.DoesNotExist:
            aluno = wm.Aluno()
            pedido = paf.PedidoForm()

        html_variables = {
            'pedido': pedido,
            'aluno': aluno,
        }
        return render(request, 'politicas_afirmativas/uerj1.html', html_variables)
    else:
        return render(request, 'common/404.html')
