# coding=utf-8
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from reportlab.pdfgen import canvas
from reportlab.lib import units
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


def home(request):

    return render(request, 'reports/index.html')


def alunos_telefones(request):
    """
    Generates a PDF file of a MS Access-like report with names and phone numbers for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':

        alunos_per_page = 38
        try:
            response = startpdffile(filename="somefilename.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="somefilename.pdf")
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


def alunos_portaria(request):
    """
    Generates a PDF file of a MS Access-like report with names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = startpdffile(filename="somefilename.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="somefilename.pdf")
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


def alunos_presenca(request):
    """
    Generates a PDF file of a MS Access-like report with CPFs, names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = startpdffile(filename="somefilename.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="somefilename.pdf")
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


def voluntarios_portaria(request):
    """
    Generates a PDF file of a MS Access-like report with CPFs, names and signatures for all students enrolled.
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            response = startpdffile(filename="somefilename.pdf", attachment=request.GET[u'attach'])
        except MultiValueDictKeyError:
            response = startpdffile(filename="somefilename.pdf")
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
        ), "%s" % (i.nome,), "%s" % (' ',), ] for i in wm.Voluntario.objects.all()]

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
