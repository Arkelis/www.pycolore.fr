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

J'ai créé un petit dépôt grâce au service [Fedora COPR](https://copr.fedorainfracloud.org/)
pour des programmes qui ne sont ni dans le dépôt officiel de Fedora, ni dans le dépôt RPM Fusion,
ou bien parce qu'il ne propose pas de dépôt individuel DNF. Le dépôt contient à ce jour deux
logiciels (voir la liste en bas de page).

**Versions de Fedora supportées** :

* Fedora 28 (Twenty Eight)
* Fedora 29 (Twenty Nine)
* Fedora 30 (Thirty)

# Installation

Le dépôt ne marche que sur les distributions citées précédemment. L'installation du dépôt se
fait facilement grâce à l'intégration dans DNF de COPR.

```
$ sudo dnf copr enable arkelis/Pycolore
```

# Installation des programmes

Vous pouvez maintenant installer les programmes de PyColore avec un simple :

```
$ sudo dnf install <nom-du-paquet-rpm>
```

La liste des programme est indiquée ci-dessous.


| **Logiciel (nom du paquet RPM)** | **Version** | **Description**                  | **Développeur**                                                   |
|:---------------------------------|:------------|:---------------------------------|:------------------------------------------------------------------|
| GitKraken (gitkraken) (en cours d'empaquetage)           | 5.0.4       | Client graphique Git élaboré     | [Axosoft, LLC.](https://www.gitkraken.com/)                       |
| Simple DNF (simple-dnf) (temporairement indisponible)         | alpha       | Client graphique DNF minimaliste | [Hyacinthe Pierre Friedrichs](http://3615.hyakosm.net/portfolio/) |
| Yaru (yaru) | r29 | Thème pour Gnome développé par la communauté Ubuntu (Community theme) | [Communauté Ubuntu](https://github.com/ubuntu/yaru) |
