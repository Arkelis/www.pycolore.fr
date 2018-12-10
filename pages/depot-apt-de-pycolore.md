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

**Distributions supportées :**

* Debian 9 (Stretch)
* Ubuntu 18.04 LTS (Cosmic Cuttlefish)
* Linux Mint 19 (Tarra)

# Installation

Le dépôt ne marche que sur les distributions utilisant APT comme gestionnaire de dépendances et pour l'architecture 64-bit.
Attention, seule les distributions indiquées précédemment sont supportées.

Pour Ubuntu 18.04 Linux Mint 19 :

```
$ echo "deb http://repo.pycolore.fr/deb cosmic main amd64" | sudo tee /etc/apt/sources.list.d/pycolore.list
```

Pour Debian 9 :

```
$ echo "deb http://repo.pycolore.fr/deb stretch main amd64" | sudo tee /etc/apt/sources.list.d/pycolore.list
```

Il faut ensuite ajouter la clé publique du dépôt qui signe les paquets.

```
$ sudo apt-key add http://repo.pycolore.fr/deb/KEY.gpg
```

# Liste des programmes

|**Logiciel (nom du paquet DEB)** | **Version** |
|:--------------------------------|:------------|
|GitKraken (gitkraken)            | 4.1.1       |

