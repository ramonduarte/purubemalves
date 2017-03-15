from django.shortcuts import render, redirect
from alunos import models as am
from projeto_redacao import models as prm
from politicas_afirmativas import models as pam
from politicas_afirmativas import forms as paf
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    try:
        perfil = am.PerfilDeAluno.objects.get(user__id=request.user.id)
    except am.PerfilDeAluno.DoesNotExist:
        return render(request, 'common/403.html')

    html_variables = {
        'name': perfil.aluno.get_nome()
    }
    return render(request, 'alunos/home.html', html_variables)


@login_required
def isencao(request):
    try:
        perfil = am.PerfilDeAluno.objects.get(user__id=request.user.id)
    except am.PerfilDeAluno.DoesNotExist:
        return render(request, 'common/403.html')

    pedido = pam.PedidoDeIsencaoUERJ.objects.get(aluno=perfil.aluno)
    form = paf.PedidoForm(instance=pedido)
    html_variables = {
        'name': perfil.aluno.get_nome(),
        'pedido': pedido,
        'form': form,
    }
    return render(request, 'alunos/isencao.html', html_variables)


@login_required
def redacao(request):
    try:
        perfil = am.PerfilDeAluno.objects.get(user__id=request.user.id)
    except am.PerfilDeAluno.DoesNotExist:
        return render(request, 'common/403.html')

    redacoes = prm.Redacao.objects.filter(aluno=perfil.aluno)
    html_variables = {
        'name': perfil.aluno.get_nome(),
        'redacoes': [i for i in redacoes],
    }

    return render(request, 'alunos/redacao.html', html_variables)


def redirect_to_home(request):
    return redirect('/alunos/home')
