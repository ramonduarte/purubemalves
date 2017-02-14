from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def contato(request):
    return render(request, 'home/contato.html')


def equipe(request):
    return render(request, 'home/equipe.html')


# def estude(request):
#     return render(request, 'home/estude.html')


def curso(request):
    return render(request, 'home/curso.html')


def resultados(request):
    return render(request, 'home/resultados.html')
