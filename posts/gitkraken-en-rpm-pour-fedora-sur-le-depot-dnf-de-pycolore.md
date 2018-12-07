<!--
.. title: GitKraken en RPM pour Fedora sur le dépôt DNF de PyColore
.. slug: gitkraken-en-rpm-pour-fedora-sur-le-depot-dnf-de-pycolore
.. date: 2018-12-07 23:49:48 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->


[GitKraken](https://www.gitkraken.com/git-client) est un client graphique pour Git. Il est plutôt bien fait
mais malheureusement il n'existe pas de RPM GitKraken dans les dépôt RPM Fusion (encore moins sur les dépôts 
officiels car c'est un logiciel propriétaire). La procédure d'installation est du coup assez
[fastidieuse](https://gist.github.com/aelkz/17528d2f6a5db73185c7dfbd28e49d18), je me suis donc créé un petit
dépôt où j'ai empaqueté GitKraken !<!-- TEASER_END -->

# Activation du dépôt

La procédure est indiquée sur [la page de présentation du dépôt DNF](https://www.pycolore.fr/depot-dnf).
Pour l'instant il ne contient que GitKraken.

```
$ curl --silent --location http://repo.pycolore.fr/rpm/pycolore.repo | sudo tee /etc/yum.repos.d/pycolore.repo
```

# Installation de GitKraken avec DNF

Il suffit de faire :

```
$ sudo dnf install gitkraken
```

Il apparaîtra dans la liste des applications une fois installé !