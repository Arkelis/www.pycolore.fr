<!--
.. title: GitKraken en RPM pour Fedora sur le dépôt DNF de PyColore
.. slug: gitkraken-en-rpm-pour-fedora-sur-le-depot-dnf-de-pycolore
.. date: 2018-12-07 23:49:48 UTC+01:00
.. tags: GNU/Linux, Fedora
.. category: Ressource
.. link: 
.. description: 
.. type: text
-->


[GitKraken](https://www.gitkraken.com/git-client) est un client graphique pour Git. Il est plutôt bien fait
mais malheureusement il n'existe pas de RPM GitKraken dans les dépôt RPM Fusion (encore moins sur les dépôts 
officiels de Fedora car c'est un logiciel propriétaire). La procédure d'installation est du coup assez
[fastidieuse](https://gist.github.com/aelkz/17528d2f6a5db73185c7dfbd28e49d18), je me suis donc créé un petit
dépôt où j'ai empaqueté GitKraken !<!-- TEASER_END -->

# Activation du dépôt

La procédure est indiquée sur [la page de présentation du dépôt DNF](https://www.pycolore.fr/depot-dnf). Le dépôt
fonctionne pour **Fedora 29** et pour l'instant, il ne contient que GitKraken.

```
$ curl --silent --location http://repo.pycolore.fr/rpm/pycolore.repo | sudo tee /etc/yum.repos.d/pycolore.repo
```

# Installation de GitKraken avec DNF

Pour installer le logiciel, il suffit de faire :

```
$ sudo dnf install gitkraken
```

et GitKraken apparaîtra dans la liste des applications une fois installé !

# Installation de GitKraken directement avec le paquet RPM

Si vous ne voulez pas activer le dépôt PyColore, vous pouvez simplement télécharger le paquet RPM et l'installer.

```
$ sudo dnf install http://repo.pycolore.fr/rpm/x86_64/gitkraken-4.1.1-1.rc3.fc29.x86_64.rpm
```

Attention, le lien peut avoir changé depuis la publication de l'article. Vous pouvez télécharger le paquet RPM
directement grâce à votre navigateur internet en vous rendant à l'adresse [http://repo.pycolore.fr/rpm/x86_64/](http://repo.pycolore.fr/rpm/x86_64/).