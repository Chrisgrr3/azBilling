from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def mca(request):
    return render(request, 'mca.html')


def mosp(request):
    return render(request, 'mosp.html')


def ea(request):
    return render(request, 'ea.html')


def mpa(request):
    return render(request, 'mpa.html')
