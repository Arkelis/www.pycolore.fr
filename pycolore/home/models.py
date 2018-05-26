from django.db import models


class Page(models.Model):
    """Petit modèle pour les pages d'accueil.

    Ils contiennent :
    titre -- le titre de la page
    contenu -- le conteu au format HTML
    slug -- la fin de l'url
    """

    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    slug = models.SlugField(max_length=100, null=True)

    def __str__(self):
        return self.titre
