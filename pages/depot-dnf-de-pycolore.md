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
ni dans le dépôt RPM Fusion, ou bien parce qu'il ne propose pas de dépôt individuel DNF. Pour
l'instant, seul GitKraken fait partie de ce dépôt.

**Versions de Fedora supportées** :

* Fedora 29 (Twenty Nine)

# Installation

Le dépôt ne marche que sur les distributions utilisant DNF comme gestionnaire de dépendances (Fedora).

```
$ curl --silent --location http://repo.pycolore.fr/rpm/pycolore.repo | sudo tee /etc/yum.repos.d/pycolore.repo
```

Attention, les paquets ne sont pour l'instant pas signés.

# Liste des programmes

|**Logiciel (nom du paquet RPM)** | **Version** |
|:------------------------------|:------------|
|GitKraken (gitkraken)        | 4.1.1       |

