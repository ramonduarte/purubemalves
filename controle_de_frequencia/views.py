from django.shortcuts import render
from website.models import Aluno, Voluntario
from controle_de_frequencia import models as cf
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('controle_de_frequencia/home.html')


def alunos(request):
    turmaa = [(i.nome, i.id) for i in Aluno.objects.all() if i.turma == u'A']
    turmab = [(i.nome, i.id) for i in Aluno.objects.all() if i.turma == u'B']
    turmac = [(i.nome, i.id) for i in Aluno.objects.all() if i.turma == u'C']
    turmad = [(i.nome, i.id) for i in Aluno.objects.all() if i.turma == u'D']

    html_variables = {
        u'alunos': u'1',
        u'voluntarios': u'',
        u'turmaA': turmaa,
        u'turmaB': turmab,
        u'turmaC': turmac,
        u'turmaD': turmad,
    }
    return render(request, 'controle_de_frequencia/alunos.html', html_variables)


def voluntarios(request):
    listof_voluntarios = [(i.nome, i.id) for i in Voluntario.objects.all() if i.is_ativo]
    html_variables = {
        u'alunos': u'',
        u'voluntarios': u'1',
        u'listof_voluntarios': listof_voluntarios,
    }
    return render(request, 'controle_de_frequencia/voluntarios.html', html_variables)


def post(request):
    if request.method == 'POST':
        if u'alunos' in request.POST:
            listof_alunos = [int(i) for i in request.POST.keys() if i.isdigit()]
            lista_de_presenca_alunos = cf.ListaDePresencaDeAlunos()
            lista_de_presenca_alunos.save()
            lista_de_presenca_alunos.aluno.add(*listof_alunos)
            lista_de_presenca_alunos.save()
        if u'voluntarios' in request.POST:
            listof_voluntarios = [int(i) for i in request.POST.keys() if i.isdigit()]
            lista_de_presenca_voluntarios = cf.ListaDePresencaDeVoluntarios()
            lista_de_presenca_voluntarios.save()
            lista_de_presenca_voluntarios.voluntario.add(*listof_voluntarios)
            lista_de_presenca_voluntarios.save()
        return render(request, 'controle_de_frequencia/post.html')
    else:
        return render_to_response('common/404.html')
