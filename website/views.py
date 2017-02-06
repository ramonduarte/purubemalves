# coding=utf-8
from django.shortcuts import render
from website import models
from django.db import transaction
import io
import datetime


# Create your views here.
def updatedb(request):
    arch_alunos_path = 'D:\Users\Ramon\Documents\Alunos.txt'
    arch_alunos = io.open(arch_alunos_path, encoding='cp1252')
    formatof_alunos = {
        u'cpf': 0,
        u'nome': 1,
        u'data de nascimento': 2,
        u'endereço': 3,
        u'complemento': 4,
        u'bairro': 5,
        u'cep': 6,
        u'cidade': 7,
        u'estado': 8,
        u'telefone': 9,
        u'email': 10,
        u'língua estrangeira': 11,
        u'turma': 12,
        u'curso pretendido': 13,
    }

    linguas_estrangeiras = {
        u'ESPANHOL': u'Espanhol',
        u'INGLÊS': u'Inglês',
        u'FRANCÊS': u'Francês',
        u'': u'Espanhol',
    }

    arch_alunos.seek(0)
    listof_alunos = [i.replace("'", "").split(';') for i in arch_alunos.readlines()]
    # print listof_alunos[1]

    # with transaction.atomic():  # Saving everything in only one transaction
    for i in listof_alunos:
        print i[formatof_alunos[u'nome']]
        if 'ESPERA' in i[formatof_alunos[u'turma']]:
            continue
        if 'A' in i[formatof_alunos[u'turma']] or 'B' in i[formatof_alunos[u'turma']]:
            # print i[formatof_alunos[u'nome']]
            new_telefone = models.Telefone(num=str(i[formatof_alunos[u'telefone']]))
            new_telefone.save()

            # Aluno was selected to be a student at PU
            new_aluno = models.Aluno(
                cpf=int(i[formatof_alunos[u'cpf']]),
                nome=i[formatof_alunos[u'nome']],
                data_de_nascimento='%s-%s-%s' % (
                    str(i[formatof_alunos[u'data de nascimento']][-4:]),
                    str(i[formatof_alunos[u'data de nascimento']][3:-5]),
                    str(i[formatof_alunos[u'data de nascimento']][:2]),
                ),
                endereco=i[formatof_alunos[u'endereço']],
                # telefone=new_telefone,
                complemento=i[formatof_alunos[u'complemento']] or u'',
                bairro=i[formatof_alunos[u'bairro']],
                cep=int(i[formatof_alunos[u'cep']].replace('-', '')),
                cidade=i[formatof_alunos[u'cidade']],
                estado=i[formatof_alunos[u'estado']][:2],
                email=i[formatof_alunos[u'email']],
                turma=i[formatof_alunos[u'turma']][0],
                lingua_estrangeira=linguas_estrangeiras[i[formatof_alunos[u'língua estrangeira']]],
                # curso_pretendido=str(i[formatof_alunos[u'curso pretendido']]).replace("'", "").decode().encode('cp1252'),
                ano_letivo=2017,
            )
            # print type(new_aluno.data_de_nascimento)
            new_aluno.save()
            # new_aluno.data_de_nascimento = datetime.datetime.today()

            new_aluno.telefone.add(new_telefone)
            # new_telefone.save()

    from django.http import HttpResponse
    return HttpResponse('huehuehue')


def updatenewdb(request):
    arch_vol_path = 'D:\Users\Ramon\Documents\Professores.txt'
    arch_vol = io.open(arch_vol_path, encoding='cp1252')
    formatof_vol = {
        u'cpf': 0,
        u'nome': 1,
        u'data de nascimento': 2,
        u'endereço': 3,
        u'complemento': 4,
        u'bairro': 5,
        u'cep': 6,
        u'cidade': 7,
        u'estado': 8,
        u'telefone': 9,
        u'email': 10,
        u'graduação': 11,
        u'equipe': 12,
        u'facebook': 13,
    }

    arch_vol.seek(0)
    listof_vols = [i.replace("'", "").split(';') for i in arch_vol.readlines()]

    # with transaction.atomic():  # Saving everything in only one transaction
    for i in listof_vols:
        print i[formatof_vol[u'nome']]
        is_ativo = True

        # Voluntario is currently work for PU
        if 'AFASTAD' in i[formatof_vol[u'equipe']]:
            is_ativo = False
            i[formatof_vol[u'equipe']] = u'Coordenação Pedagógica'

        new_telefone = models.Telefone(num=str(i[formatof_vol[u'telefone']]))
        new_telefone.save()

        # new_equipe = models.Equipe.objects.get(nome=i[formatof_vol[u'equipe']])

        new_vol = models.Voluntario(
            cpf=int(i[formatof_vol[u'cpf']]),
            nome=i[formatof_vol[u'nome']],
            data_de_nascimento='%s-%s-%s' % (
                str(i[formatof_vol[u'data de nascimento']][-4:]),
                str(i[formatof_vol[u'data de nascimento']][3:-5]),
                str(i[formatof_vol[u'data de nascimento']][:2]),
            ),
            endereco=i[formatof_vol[u'endereço']],
            complemento=i[formatof_vol[u'complemento']] or u'',
            bairro=i[formatof_vol[u'bairro']],
            cep=int(i[formatof_vol[u'cep']].replace('-', '')),
            cidade=i[formatof_vol[u'cidade']],
            estado=i[formatof_vol[u'estado']][:2],
            email=i[formatof_vol[u'email']],
            is_ativo=is_ativo,
            facebook=i[formatof_vol[u'facebook']],
            # equipe=new_equipe,
        )
        # print type(new_aluno.data_de_nascimento)
        new_vol.save()
        # new_aluno.data_de_nascimento = datetime.datetime.today()

        new_vol.telefone.add(new_telefone)
        # new_telefone.save()

    from django.http import HttpResponse
    return HttpResponse('done')
