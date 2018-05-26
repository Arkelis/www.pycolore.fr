from django.shortcuts import render
from .models import Page
# from django.http import HttpResponse


def accueil(request):
    """Page d'accueil du site"""
    page = Page.objects.get(titre='Bienvenue sur Pycolore !')
    context = {'titre': page.titre, 'contenu': page.contenu}
    return render(request, 'home/index.html', context)
