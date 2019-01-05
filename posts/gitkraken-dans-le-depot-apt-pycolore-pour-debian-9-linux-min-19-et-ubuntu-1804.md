<!--
.. title: GitKraken dans le dépôt APT PyColore pour Debian 9, Linux Min 19 et Ubuntu 18.04
.. slug: gitkraken-dans-le-depot-apt-pycolore-pour-debian-9-linux-min-19-et-ubuntu-1804
.. date: 2018-12-10 22:37:58 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

Après la création du [dépôt DNF](https://www.pycolore.fr/depot-dnf) et la mise en 
ligne du [RPM de GitKraken](../gitkraken-en-rpm-pour-fedora-sur-le-depot-dnf-de-pycolore/), PyColore
dispose maintenant également d'un dépôt APT, avec le même programme ! Ainsi PyColore
possède un dépôt fonctionnel avec Fedora 29, Linux Mint 19, Debian 9 et Ubuntu 18.04.

En fait, il existe un paquet DEB pour GitKraken sur le site officiel mais il n'est dans
aucun dépôt (donc mise à jour fastidieuse) et il avait un petit problème de dépendance que
j'ai résolu (du moins je l'espère).<!-- TEASER_END -->

# Activation du dépôt

On suit la [procédure d'installation du dépôt APT](https://www.pycolore.fr/depot-apt). Pour 
Linux Mint 19 et Ubuntu 18.04 :

```
$ sudo sh -c 'echo "deb http://repo.pycolore.fr/deb bionic main" > /etc/apt/sources.list.d/pycolore.list'
$ wget -qO - http://repo.pycolore.fr/deb/KEY.gpg | sudo apt-key add -
$ sudo apt update
```

Pour Debian 9 :

```
$ sudo sh -c 'echo "deb http://repo.pycolore.fr/deb stretch main" > /etc/apt/sources.list.d/pycolore.list'
$ wget -qO - http://repo.pycolore.fr/deb/KEY.gpg | sudo apt-key add -
$ sudo apt update
```

# Installation de GitKraken

```
$ sudo apt install gitkraken
```