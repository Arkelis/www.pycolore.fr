<!--
.. title: Projet Python : Convertisseur Latex vers HTML (et CSS)
.. slug: projet-python-convertisseur-latex-vers-html-et-css
.. date: 2018-04-21 20:45:41 UTC+02:00
.. tags: mathjax, Python, LaTeX, HTML, KaTeX
.. category: Projets
.. link:
.. description:
.. type: text
-->

## Objectif

Pour l'instant, les fichiers LaTeX ne sont lisibles que via le téléchargement des fichiers PDF. Pour ne pas avoir à les faire télécharger, je suis en train de travailler (à rythme irrégulier) sur un **convertisseur LaTeX > HTML** écrit en **Python**.<!-- TEASER_END --> Les objectifs sont de créer un fichier HTML "lisible", accompagné d'un fichier CSS, pour mettre en forme les définitions par exemple, et de manière générale pour faire des pages esthétiques. L'implémentation des équations se fera avec KaTeX, qui est d'ailleurs pris en charge par Nikola : $\mathrm{e}^{i\pi}=-1$.

## Questionnements
### CSS ou Bootstrap

Au fur et à mesure que je découvre le développement Web, je me demande s'il est vraiment nécessaire de créer un fichier CSS, un thème Bootstrap sobre pourrait faire l'affaire, ça fera moins de travail ! La création d'un CSS est cependant plus formatrice.

### HTML vs Markdown

Pour faire plus simple, l'utilisation du Markdown peut être une alternative, mais on est restreint dans la mise en forme.

## Le projet sur GitHub

Vous pouvez suivre l'avancement et/ou contribuer en vous rendant sur la [page GitHub](http://arkelis.github.io/latex_to_html).
