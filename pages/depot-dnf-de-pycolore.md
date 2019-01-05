<!--
.. title: Dépôt DNF de PyColore
.. hidetitle: yes
.. slug: depot-dnf
.. date: 2018-12-06 23:20:28 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

<h1 class="page-title">Dépôt DNF de PyColore</h1>
<hr class="title-hr">

J'ai créé un petit dépôt pour des programmes qui ne sont ni dans le dépôt officiel de Fedora,
ni dans le dépôt RPM Fusion, ou bien parce qu'il ne propose pas de dépôt individuel DNF. Le dépôt
contient à ce jour deux logiciels (voir la liste en bas de page).

**Versions de Fedora supportées** :

* Fedora 29 (Twenty Nine)

# Installation

Le dépôt ne marche que sur les distributions utilisant DNF comme gestionnaire de dépendances (Fedora).
Dans un terminal&nbsp;:

```
$ curl --silent --location http://repo.pycolore.fr/rpm/pycolore.repo | sudo tee /etc/yum.repos.d/pycolore.repo
```

Attention, les paquets ne sont pour l'instant pas signés.

# Installation des programmes

Vous pouvez maintenant installer les programmes de PyColore avec un simple :

```
$ sudo dnf install <nom-du-paquet-rpm>
```

La liste des programme est indiquée ci-dessous.


| **Logiciel (nom du paquet RPM)** | **Version** | **Description**                  | **Développeur**                                                   |
|:---------------------------------|:------------|:---------------------------------|:------------------------------------------------------------------|
| GitKraken (gitkraken)            | 4.1.1       | Client graphique Git élaboré     | [Axosoft, LLC.](https://www.gitkraken.com/)                       |
| Simple DNF (simple-dnf)          | alpha       | Client graphique DNF minimaliste | [Hyacinthe Pierre Friedrichs](http://3615.hyakosm.net/portfolio/) |