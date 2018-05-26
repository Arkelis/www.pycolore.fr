from django.shortcuts import render
from .models import Page
# from django.http import HttpResponse


def index(request):
    """Page d'accueil du site"""
    page = Page.objects.get(slug='index')
    context = {'titre': page.titre, 'contenu': page.contenu}
    return render(request, 'home/index.html', context)


def page(request, slug):
    """Pages du site vitrine"""
    page = Page.objects.get(slug=slug)
    context = {'titre': page.titre, 'contenu': page.contenu}
    return render(request, 'home/index.html', context)
