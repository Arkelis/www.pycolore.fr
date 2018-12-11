<!--
.. title: Dépôt APT de PyColore
.. hidetitle: yes
.. slug: depot-apt
.. date: 2018-12-06 23:20:28 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

<h1 class="page-title">Dépôt APT de PyColore</h1>
<hr class="title-hr">

J'ai créé un petit dépôt pour Debian et Linux Mint qui contient des programmes qui ne sont pas 
dans les dépôts officiels. Pour l'instant il n'y a que GitKraken dans ce dépôt.

# Distributions supportées

* Debian 9 (Stretch)
* Ubuntu 18.04 LTS (Bionic Beaver)
* Linux Mint 19 (Tarra)

# Installation

Le dépôt ne marche que sur les distributions utilisant APT comme gestionnaire de dépendances.
Attention, seule les distributions indiquées précédemment sont supportées.

L'installation se déroule en trois étapes&nbsp;:

1. Indiquer la nouvelle source de logiciels PyColore ;
2. Importer la clé qui signe les dépôts de la nouvelle source ;
3. Mettre à jour le cache d'APT.

## Ubuntu 18.04 et Linux Mint 19
### En ligne de commande

Dans un terminal&nbsp;:

```
$ sudo sh -c 'echo "deb http://repo.pycolore.fr/deb bionic main" > /etc/apt/sources.list.d/pycolore.list'
$ wget -qO - http://repo.pycolore.fr/deb/KEY.gpg | sudo apt-key add -
$ sudo apt update
```

### En graphique (indications pour Linux Mint)

Sur Linux Mint, ouvrez "Sources de logiciels" et allez dans l'onglet "Dépôts supplémentaires".
Cliquez sur le bouton "Ajouter un dépôt" et renseignez `deb http://repo.pycolore.fr/deb bionic main`
comme ci-dessous&nbsp;:

<figure class="text-center">
<img src="/assets/img/mint_apt_sources.png"
     alt="Sources de Logiciels"
     width="70%" />
    <figcaption>Ajout du dépôt PyColore</figcaption>
</figure>

Ensuite rendez vous à l'URL http://repo.pycolore.fr/deb dans votre navigateur et téléchargez `KEY.gpg`.
Il s'agit d'une clé [gpg](https://doc.ubuntu-fr.org/gnupg) qui permet de signer les paquets et donc de vérifier
que les paquets que vous téléchargez ont bien été créés sur PyColore.

Retournez dans Sources de logiciels et allez à l'onglet "Clefs d'authentification". Cliquez sur le bouton
"Importer un fichier clé" et sélectionner `KEY.gpg` que vous venez de télécharger. La nouvelle clé apparaît :

<figure class="text-center">
<img src="/assets/img/mint_apt_sources_2.png"
     alt="Sources de Logiciels"
     width="70%" />
    <figcaption>Ajout de la clé du dépôt PyColore</figcaption>
</figure>

Vous pouvez maintenant cliquer sur le bouton "OK" du bandeau vert indiquant que la configuration a changé et
qu'il faut mettre à jour le cache.

## Debian 9

Dans un terminal&nbsp;:

```
$ sudo sh -c 'echo "deb http://repo.pycolore.fr/deb stretch main" > /etc/apt/sources.list.d/pycolore.list'
$ wget -qO - http://repo.pycolore.fr/deb/KEY.gpg | sudo apt-key add -
$ sudo apt update
```

# Installation des programmes

Vous pouvez maintenant installer les programmes de PyColore avec un simple :

```
$ sudo apt install <nom-du-paquet-deb>
```

La liste des programme est indiquée ci-dessous.


| **Logiciel (nom du paquet DEB)** | **Version** |
|:---------------------------------|:------------|
| GitKraken (gitkraken)            | 4.1.1       |

