<!--
.. title: Utiliser Bash sous Windows
.. slug: utiliser-bash-sous-windows
.. date: 2018-08-04 15:20:46 UTC+02:00
.. tags: Cmder, GNU/Linux, Windows
.. category: Mémo
.. link: https://www.pycolore.fr/posts/utiliser-bash-sous-windows
.. description: Installer Bash, GNU Make, rsync et GnuPG sur Windows grâce à Cmder et MSYS2.
.. type: text
-->

Pour le développement, les meilleurs outils sont les outils GNU, en général pas disponibles pour Windows&nbsp;! Heureusement il existe de nombreux portages. <!-- TEASER_END -->

# Installer le terminal Bash avec Cmder

Windows propose un sous-système Linux pour utiliser Bash. Cependant, installer tout un système juste pour avoir accès à quelques commandes c'est cher payé... On va plutôt installer un merveilleux outil&nbsp;: [Cmder](http://cmder.net/)&nbsp;! On va utiliser le gestionnaire de paquets Windows Chocolatey (cf. [l'installation du serveur Apache sur Windows](../../blog/installer-un-serveur-web-sur-windows-sans-wamp)).

```powershell
PS > choco.exe install cmder
```

Il va l'installer dans un dossier `tools` à la racine de votre disque (par exemple `C:\tools\cmder`) Pour pouvoir lancer facilement Cmder, on peut ajouter son exécutable au PATH Windows. Pour cela on recherche `Path` dans le menu démarrer puis on clique sur "Modifier les variables d'environnement Système" > "Variables d'environnement..." > "Variables système" > Double clic sur "Path", puis on ajoute le chemin vers le dossier de l'exécutable `cmder.exe`. Une fois ce changement appliqué, il y a juste à taper `cmder` dans le menu démarrer ou bien faire Windows+R (Exécuter...) et taper la même commande pour le lancer&nbsp;!

Si on lance Cmder, il nous démarre une session CMD, mais nous on veut bash, c'est quand même plus cool quand on aime Linux. Dans les paramètres (clic sur l'icône Lambda > "Settings" > "Startup") on choisit `{bash::bash}` comme "Specified named task". Quand on lance Cmder, on arrive alors devant ça&nbsp;:

<figure class="text-center">
    <img src="/assets/img/cmder.jpg" alt="Fenêtre Cmder" width="75%" />
    <figcaption>Le lambda ce Cmder nous invite à taper une commande.</figcaption>
</figure>

Git pour Windows vient embarqué avec Cmder, on a donc un tas de commandes disponibles comme `git`, et puis plein de commandes UNIX comme `ls` et compagnie. Pour le SSH, j'avais déjà activé le client Windows OpenSSH, donc je ne sais pas si ça marche sans l'activer.

# Installer GNU Make

Une commande bien pratique disponible sur GNU/Linux est [GNU Make](https://www.gnu.org/software/make/) pour exécuter des recettes afin d'automatiser des choses (compilation, déploiement...) mais il n'existe pas d'exécutables officiels pour Windows. Du coup on utilise un dépôt fort pratique&nbsp;: [MSYS2](http://repo.msys2.org/msys/) (i686 pour les ordinateurs 32-bit et x86_64 pour 64-bit). Ce dépôt a l'avantage d'avoir une version à jour de `make`. En fait, Git embarqué par Cmder utilise MSYS2, donc tout ce qu'on télécharge ici fonctionnera bien avec Cmder. Au moment où j'écris ce Mémo, la dernière version de `make` est la 4.2.1, on télécharge donc `make-4.2.1-1-x86_64.pkg.tar.xz` (les fichiers en .sig sont des signatures). On extrait le contenu du dossier `usr` et on le colle dans le dossier `usr` du Git de Cmder, normalement à l'emplacement `C:\tools\cmder\vendor\git-for-windows`. Voilà&nbsp;! On a bien `make` fonctionnel&nbsp;:

```bash
λ make --version
GNU Make 4.2.1
Construit pour x86_64-pc-msys
Copyright (C) 1988-2016 Free Software Foundation, Inc.
Licence GPLv3+ : GNU GPL version 3 ou ultérieure <http://gnu.org/licenses/gpl.html>
Ceci est un logiciel libre : vous êtes autorisé à le modifier et à la redistribuer.
Il ne comporte AUCUNE GARANTIE, dans la mesure de ce que permet la loi.
```

# Installer rsync

Git vient avec SSH, mais [rsync](https://rsync.samba.org/) manque à l'appel, on le trouve aussi dans le dépôt de MSYS2 et on procède de la même manière.

```bash
λ rsync --version
rsync  version 3.1.3  protocol version 31
Copyright (C) 1996-2018 by Andrew Tridgell, Wayne Davison, and others.
Web site: http://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, hardlinks, symlinks, IPv6, batchfiles, inplace,
    append, ACLs, no xattrs, iconv, symtimes, prealloc

rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
are welcome to redistribute it under certain conditions.  See the GNU
General Public Licence for details.
```

# Installer GnuPG

Le `gnupg` ([GNU Privacy Gard](https://gnupg.org/)) fourni avec Cmder est un peu vieux. Comme il existe des binaires de GnuPG pour Windows sur Chocolatey, on va en profiter et les installer.

```bash
λ choco install gnupg-modern
```

Pour que `git` utilise bien le `gpg` que l'on veut, il faut lui indiquer&nbsp;:

```bash
λ git config --global gpg.program "C:\Program Files (x86)\gnupg\bin\gpg.exe"
```

On doit aussi complètement supprimer le GnuPG fourni avec Cmder qui se trouve dans le dossier `vendor` de ce dernier, sinon lorsque l'on appellera la commande `gpg` dans Cmder, il nous sortira l'ancien. Si on ne veut pas le supprimer, il faut remonter le chemin du GnuPG récent dans le PATH pour qu'il soit trouvé avant.

```bash
λ gpg --version
gpg (GnuPG) 2.2.9
libgcrypt 1.8.3
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: D:/home/guillaume/AppData/Roaming/gnupg
Algorithmes pris en charge :
Clef publique : RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Chiffrement : IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256,
              TWOFISH, CAMELLIA128, CAMELLIA192, CAMELLIA256
Hachage : SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression : Non compressé, ZIP, ZLIB, BZIP2
```

# À propos de MSYS2

On peut ainsi, avec Chocolatey et MSYS2 avoir accès à plein de commandes GNU/Unix&nbsp;! [MSYS2](http://www.msys2.org/) est un projet qui a pour but de porter un tas de commandes Unix vers Windows. C'est un véritable mini-système, qui, si on l'installe à partir du site, vient avec `pacman`, le gestionnaire de paquets d'Arch Linux. J'ai choisi ici de télécharger les commandes voulues à la main, c'est moins facile à maintenir après, mais ça évite de devoir installer entièrement MSYS2 alors que Git pour Windows vient avec. (On peut essayer sinon Cmdermini + MSYS2 mais ils ne se lient pas aussi bien.) Il faut garder en tête les commandes que l'on a installées pour les mettre à jour et les réinstaller au cas où une mise à jour de Cmder ne les vire.
