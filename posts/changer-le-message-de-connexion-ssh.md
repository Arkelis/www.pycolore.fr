---
title: Changer le message de connexion SSH (Debian)
slug: changer-le-message-de-connexion-ssh
date: 2018-07-18 14:56:26 UTC+02:00
tags: GNU/Linux, SSH, Debian, Serveur
category: Mémo
link: 
description: 
type: text
---

On peut facilement changer le message d'accueil que l'on voit lorsque l'on se connecte en SSH au serveur. Les opérations décrites ci-après ont été effectuées sur un serveur Debian 9 (Stretch). Debian utilise des fichiers à deux emplacements&nbsp;:

* pour un affichage dynamique à `/etc/update-motd.d/`&nbsp;: les fichiers de ce dossier sont appelés dans l'ordre alphabétique. Ce sont des scripts bash&nbsp;;
* pour un affichage statique dans le fichier `/etc/motd`, un simple fichier texte.

<!-- TEASER_END -->

# /etc/update-motd.d/

Par défaut il y a dans ce dossier un fichier `10-uname` qui comporte une commande indiquant le noyau utilisé et diverses autres informations. On peut tout à fait le modifier&nbsp;; par exemple sur le serveur PyColore, le fichier est comme ceci&nbsp;:
```bash
echo "" # pour un saut de ligne
echo "This is PyColore server."
echo ""
neofetch
```

# /etc/motd

Ce fichier comporte du simple texte qui apparaîtra après les commandes bash. Pour ma part, il indique simplement les domaines hébergés sur le serveur. Cela donne&nbsp;: 

<figure class="text-center">
    <img src="/assets/img/ssh.jpg" alt="Résultat" width="75%" />
    <figcaption>Résultat</figcaption>
</figure>
