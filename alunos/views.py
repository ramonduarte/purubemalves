from django.shortcuts import render, redirect
from website import models as wm
from alunos import models as am
from projeto_redacao import models as prm
from politicas_afirmativas import models as pam
from politicas_afirmativas import forms as paf
from django.contrib.auth.decorators import login_required
from datetime import date


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

    try:
        pedido = pam.PedidoDeIsencaoUERJ.objects.get(aluno=perfil.aluno)
        form = paf.PedidoForm(instance=pedido)
        html_variables = {
            'name': perfil.aluno.get_nome(),
            'pedido': pedido,
            'form': form,
        }
    except pam.PedidoDeIsencaoUERJ.DoesNotExist:
        html_variables = {
            'name': perfil.aluno.get_nome(),
            'notfound': "nnnn",
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


@login_required
def emprestimos(request):
    try:
        perfil = am.PerfilDeAluno.objects.get(user__id=request.user.id)
    except am.PerfilDeAluno.DoesNotExist:
        return render(request, 'common/403.html')

    livros = wm.EmprestimoParaAluno.objects.filter(aluno=perfil.aluno)
    html_variables = {
        'name': perfil.aluno.get_nome(),
        'livros': [i for i in livros],
    }
    for l in html_variables['livros']:
        if l.data_de_devolucao < date.today():
            l.situacao = "Em atraso"
        else:
            l.situacao = "Dentro do prazo"
    if len(livros) == 0:
        html_variables['notfound'] = True

    return render(request, 'alunos/emprestimos.html', html_variables)


@login_required
def biblioteca(request):
    try:
        perfil = am.PerfilDeAluno.objects.get(user__id=request.user.id)
    except am.PerfilDeAluno.DoesNotExist:
        return render(request, 'common/403.html')

    livros = wm.Livro.objects.filter()
    html_variables = {
        'livros': [i for i in livros],
    }

    return render(request, 'alunos/biblioteca.html', html_variables)


def redirect_to_home(request):
    return redirect('/alunos/home')
