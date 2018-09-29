<!--
.. title: Activer les dépôts essentiels sur Fedora : RPM Fusion et UnitedRPMS
.. slug: activer-les-depots-essentiels-sur-fedora-rpm-fusion-et-unitedrpm
.. date: 2018-09-25 00:32:16 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

Lorsqu'on installe Fedora, les dépôts officiels activés par défaut ne contiennent que des logiciels libres. Pour une meilleure expérience utilisateur, il est cependant recommandé d'activer des dépôts contenant des logiciels tiers voire propriétaires. Deux dépôts connus sont [RPM Fusion](https://rpmfusion.org) et [UnitedRPMS](https://unitedrpms.github.io), que l'on va installer ici.

# Installation de RPM Fusion et de Fedy

RPM Fusion est un dépôt très connu qui contient de très nombreux programmes et librairies supplémentaires qui ne peuvent pas être présents dans les dépôts du projet Fedora (en général à cause de licences non libres). Il est indispensable de l'activer pour une meilleure expérience (notamment avec les codecs vidéo pour les navigateurs). Il existe deux sections&nbsp;: **free** (libres) et **non-free** (propriétaires).

Pour activer les deux sections, entrer cette commande dans le terminal&nbsp;:

```bash
$ sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm # free
$ sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm # non-free
```

Un petit outil graphique permet d'installer des applications de RPM Fusion facilement et d'effectuer divers tâches sur le système, il s'appelle [Fedy](https://www.folkswithhats.org). Pour l'installer&nbsp;:

```bash
$ sudo dnf install https://dl.folkswithhats.org/fedora/$(rpm -E %fedora)/RPMS/fedy-release.rpm
$ sudo dnf intall fedy
```
<figure class="text-center">
    <img src="/assets/img/ssh.jpg" alt="Interface de Fedy" width="65%" />
    <figcaption>Fedy</figcaption>
</figure>

# Installation de UnitedRPMS

Certaines applications ne se trouvent pas sur RPM Fusion (par exemple le navigateur Opéra). Il existe un autre dépôt, UnitedRPMS, contenant d'autres programmes. On peut activer ce dépôt en complément de RPM Fusion.

Pour installer UnitedRPMS&nbsp;:

```bash
$ sudo rpm --import https://raw.githubusercontent.com/UnitedRPMs/unitedrpms/master/URPMS-GPG-PUBLICKEY-Fedora-24 # import de clé GPG
$ sudo dnf -y install https://github.com/UnitedRPMs/unitedrpms/releases/download/8/unitedrpms-$(rpm -E %fedora)-8.fc$(rpm -E %fedora).noarch.rpm
```