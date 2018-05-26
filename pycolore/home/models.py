from django.db import models


class Page(models.Model):
    """Petit modèle pour les pages d'accueil.

    Ils contiennent :
    titre -- le titre de la page
    contenu -- le conteu au format HTML
    slug -- url
    """

    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
