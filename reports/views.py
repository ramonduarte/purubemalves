# coding=utf-8
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from reportlab.pdfgen import canvas
from reportlab.lib import units, pagesizes
from reportlab.platypus import tables
from django.http import HttpResponse
from website import models as wm


def startpdffile(filename="somefilename.pdf", attachment=False):
    response = HttpResponse(content_type='application/pdf')
    if attachment:
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    else:
        response['Content-Disposition'] = 'filename="' + filename + '"'
    return response


def starttextobject(canv, font="Helvetica-Oblique", fontsize=14):
    textobject = canv.beginText()
    textobject.setTextOrigin(20, 10.5 * units.inch)
    textobject.setFont(font, fontsize)

    return textobject


def startnewpage(data, style, canv, textobject):
    t = tables.Table(data=data)
    w, h = t.wrapOn(canv, 0, 0)
    t.setStyle(style)
    t.drawOn(canv, 0.75 * units.inch, 0.5 * units.inch)

    canv.drawText(textobject)
    canv.showPage()


@login_required
def home(request):

    return render(request, 'reports/index.html')


@login_required
def alunos_telefones(request):
    """
    Generates a PDF file of a MS Access-like report with names and phone numbers for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':

        alunos_per_page = 38
        try:
            response = startpdffile(filename="alunos_telefones.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="alunos_telefones.pdf")
        p = canvas.Canvas(response, pagesize='A4', pageCompression=0)
        textobject = starttextobject(p)
        textobject.textLine('ALUNOS')
        list_style = tables.TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
        ])
        header = [
            ['TURMA', '%-70s' % 'NOME', '%-40s' % 'TELEFONES']
        ]
        filler = [[' ' * 5, ' ' * 70, ' ' * 40]]

        try:
            data = [["%s" % (i.turma,), "%-70s" % (i.nome,), "%-40s" % (i.tel,), ] for i in wm.Aluno.objects.filter(
                turma=request.GET[u'turma']
            ).all()]

        except MultiValueDictKeyError:
            data = [["%s" % (i.turma,), "%-70s" % (i.nome,), "%-40s" % (i.tel,), ] for i in wm.Aluno.objects.all()]

        for i in range(0, len(data), alunos_per_page):
            startnewpage(
                data=header + data[i:i + alunos_per_page] + filler * (
                    alunos_per_page - len(data[i:i + alunos_per_page])
                ),
                style=list_style,
                canv=p,
                textobject=textobject,
            )

        p.save()
        return response

    else:
        return render(request, 'common/403.html')


@login_required
def alunos_portaria(request):
    """
    Generates a PDF file of a MS Access-like report with names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = startpdffile(filename="alunos_portaria.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="alunos_portaria.pdf")
        alunos_per_page = 38

        p = canvas.Canvas(response, pagesize='A4', pageCompression=0)
        textobject = starttextobject(p)
        textobject.textLine('ALUNOS')
        list_style = tables.TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
            # ('COLBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
        ])
        header = [
            ['TURMA', '%-70s' % 'NOME', '%-70s' % 'ASSINATURA']
        ]
        filler = [[' ' * 5, ' ' * 70, ' ' * 65]]

        try:
            data = [["%s" % (i.turma,), "%s" % (i.nome,), "%s" % (' ',), ] for i in wm.Aluno.objects.filter(
                turma=request.GET[u'turma']
            ).all()]

        except MultiValueDictKeyError:
            data = [["%s" % (i.turma,), "%s" % (i.nome,), "%s" % (' ',), ] for i in wm.Aluno.objects.all()]

        for i in range(0, len(data), alunos_per_page):
            startnewpage(
                data=header + data[i:i + alunos_per_page] + filler * (
                    alunos_per_page - len(data[i:i + alunos_per_page])
                ),
                style=list_style,
                canv=p,
                textobject=textobject,
            )

        p.save()
        return response

    else:
        return render(request, 'common/403.html')


@login_required
def alunos_presenca(request):
    """
    Generates a PDF file of a MS Access-like report with CPFs, names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = startpdffile(filename="alunos_presenca.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="alunos_presenca.pdf")
        alunos_per_page = 38

        p = canvas.Canvas(response, pagesize='A4', pageCompression=0)
        textobject = starttextobject(p)
        textobject.textLine('ALUNOS')
        list_style = tables.TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
            # ('COLBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
        ])
        header = [
            ['%-15s' % 'CPF', '%-65s' % 'NOME', '%-65s' % 'ASSINATURA']
        ]
        filler = [[' ' * 15, ' ' * 65, ' ' * 65]]

        try:
            data = [["%03i.%03i.%03i-%02i" % (
                i.cpf/100000000 % 1000, i.cpf/100000 % 1000, i.cpf/100 % 1000, i.cpf % 100,
            ), "%s" % (i.nome,), "%s" % (' ',), ] for i in wm.Aluno.objects.filter(
                turma=request.GET[u'turma']
            ).all()]

        except MultiValueDictKeyError:
            data = [["%03i.%03i.%03i-%02i" % (
                i.cpf / 100000000 % 1000, i.cpf / 100000 % 1000, i.cpf / 100 % 1000, i.cpf % 100,
            ), "%s" % (i.nome,), "%s" % (' ',), ] for i in wm.Aluno.objects.all()]

        for i in range(0, len(data), alunos_per_page):
            startnewpage(
                data=header + data[i:i + alunos_per_page] + filler * (
                    alunos_per_page - len(data[i:i + alunos_per_page])
                ),
                style=list_style,
                canv=p,
                textobject=textobject,
            )

        p.save()
        return response

    else:
        return render(request, 'common/403.html')


@login_required
def voluntarios_portaria(request):
    """
    Generates a PDF file of a MS Access-like report with CPFs, names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = startpdffile(filename="voluntarios_portaria.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="voluntarios_portaria.pdf")
        vols_per_page = 38

        p = canvas.Canvas(response, pagesize='A4', pageCompression=0)
        textobject = starttextobject(p)
        textobject.textLine('VOLUNTÁRIOS')
        list_style = tables.TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
            # ('COLBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
        ])
        header = [
            ['%-15s' % 'CPF', '%-65s' % 'NOME', '%-65s' % 'ASSINATURA']
        ]
        filler = [[' ' * 15, ' ' * 65, ' ' * 65]]

        data = [["%03i.%03i.%03i-%02i" % (
            i.cpf / 100000000 % 1000, i.cpf / 100000 % 1000, i.cpf / 100 % 1000, i.cpf % 100,
        ), "%s" % (i.nome,), "%s" % (' ',), ] for i in wm.Voluntario.objects.filter(is_ativo=True).all()]

        for i in range(0, len(data), vols_per_page):
            startnewpage(
                data=header + data[i:i + vols_per_page] + filler * (
                    vols_per_page - len(data[i:i + vols_per_page])
                ),
                style=list_style,
                canv=p,
                textobject=textobject,
            )

        p.save()
        return response

    else:
        return render(request, 'common/403.html')


@login_required
def voluntarios_contatos(request):
    """
    Generates a PDF file of a MS Access-like report with CPFs, names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = startpdffile(filename="voluntarios_contatos.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="voluntarios_contatos.pdf")
        vols_per_page = 28

        p = canvas.Canvas(response, pagesize=pagesizes.landscape(pagesizes.A4), pageCompression=0)
        textobject = starttextobject(p)
        textobject.textLine('VOLUNTÁRIOS')
        list_style = tables.TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
            # ('COLBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
        ])
        header = [
            ['%-90s' % 'EQUIPE', '%-60s' % 'NOME', '%-40s' % 'TELEFONES', '%-35s' % 'E-MAIL']
        ]
        filler = [[' ' * 90, ' ' * 60, ' ' * 40, ' ' * 35]]

        data = [
            [
                "%s, "*len(i.get_equipe()) % tuple(i.get_equipe()), "%s" % (i.nome,), "%s" % (' ',),
            ] for i in wm.Voluntario.objects.filter(is_ativo=True).all()
        ]

        for i in range(0, len(data), vols_per_page):
            startnewpage(
                data=header + data[i:i + vols_per_page] + filler * (
                    vols_per_page - len(data[i:i + vols_per_page])
                ),
                style=list_style,
                canv=p,
                textobject=textobject,
            )

        p.save()
        return response

    else:
        return render(request, 'common/403.html')


@login_required
def simulados_equerj_ata(request):
    """
    Generates a PDF file of a MS Access-like report with CPFs, names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = HttpResponse(content_type='application/pdf')
            if bool(request.GET[u'attach']):
                response['Content-Disposition'] = 'attachment; filename="simulados_equerj_ata.pdf"'
            else:
                response['Content-Disposition'] = 'filename="simulados_equerj_ata.pdf"'
        except MultiValueDictKeyError:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="simulados_equerj_ata.pdf"'

        p = canvas.Canvas(response, pagesize=pagesizes.A4, pageCompression=0)
        alunos = wm.Aluno.objects.filter(is_ativo=True).all()
        alunos_per_first_page = 30
        alunos_per_page = 42

        # Drawing report header as a picture
        imgobject = p.drawImage(
            settings.STATIC_ROOT + '\\reports\\img\\simulado_equerj_ata_bg.png',
            x=pagesizes.cm * 1.7, y=pagesizes.cm * 21.5,
            width=pagesizes.cm * 18, height=pagesizes.cm * 7,
        )

        textobject = starttextobject(p, fontsize=13)
        list_style = tables.TableStyle([
            ('ROWBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
            # ('COLBACKGROUNDS', (0, 0), (-1, -1), [tables.colors.lightgrey, tables.colors.whitesmoke]),
        ])
        header = [
            ['%-15s' % 'CPF', '%-65s' % 'NOME', '%-55s' % 'ASSINATURA']
        ]
        filler = [[' ' * 15, ' ' * 65, ' ' * 55]]

        data = [["%03i.%03i.%03i-%02i" % (
            i.cpf / 100000000 % 1000, i.cpf / 100000 % 1000, i.cpf / 100 % 1000, i.cpf % 100,
        ), "%s" % (i.nome,), "%s" % (' ',), ] for i in alunos]

        # Drawing first page, the one with the header
        startnewpage(
            data=header + data[0:alunos_per_first_page],
            style=list_style,
            canv=p,
            textobject=textobject,
        )

        # Drawing the following pages
        for k in range(alunos_per_first_page, len(data), alunos_per_page):
            startnewpage(
                data=header + data[k:k + alunos_per_page] + filler * (
                    alunos_per_page - len(data[k:k + alunos_per_page])
                ),
                style=list_style,
                canv=p,
                textobject=textobject,
            )

        p.save()
        return response

    else:
        return render(request, 'common/403.html')


@login_required
def simulados_equerj_cartao(request):
    """
    Generates a PDF file of a MS Access-like report with CPFs, names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = HttpResponse(content_type='application/pdf')
            if bool(request.GET[u'attach']):
                response['Content-Disposition'] = 'attachment; filename="simulados_equerj_cartao.pdf"'
            else:
                response['Content-Disposition'] = 'filename="simulados_equerj_cartao.pdf"'
        except MultiValueDictKeyError:
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="simulados_equerj_cartao.pdf"'

        p = canvas.Canvas(response, pagesize=pagesizes.A4, pageCompression=0)
        alunos = wm.Aluno.objects.filter(is_ativo=True).all()

        for i in alunos:
            imgobject = p.drawImage(
                settings.STATIC_ROOT + '\\reports\\img\\simulado_equerj_cartao_bg.png',
                x=pagesizes.cm * .5, y=pagesizes.cm * 9,
                width=pagesizes.cm * 20, height=pagesizes.cm * 20,
            )
            textobject = p.beginText(x=0.85 * pagesizes.cm, y=23.90 * pagesizes.cm)
            textobject.textLine("%03i.%03i.%03i-%02i" % (
                i.cpf / 100000000 % 1000, i.cpf / 100000 % 1000, i.cpf / 100 % 1000, i.cpf % 100,
                ))

            textobject.setTextOrigin(x=4.7 * pagesizes.cm, y=23.95 * pagesizes.cm)
            textobject.textLine(i.nome)

            textobject.setTextOrigin(x=16.5 * pagesizes.cm, y=23.75 * pagesizes.cm)
            textobject.textLine(i.lingua_estrangeira.upper())
            p.drawText(textobject)
            p.showPage()

        p.save()
        return response

    else:
        return render(request, 'common/403.html')
