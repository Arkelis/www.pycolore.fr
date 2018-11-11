<!--
.. title: Installer Linux Mint à côté de Windows en dual boot
.. slug: installer-linux-a-cote-de-windows-dual-boot
.. date: 2018-09-20 11:36:00 UTC+02:00
.. tags: GNU/Linux, Mint
.. category: Mémo
.. link: 
.. description: 
.. type: text
-->

Ce guide vous permettra d'installer pas à pas Linux sur votre ordinateur. Si vous lisez ceci, c'est probablement que vous n'avez pas encore installé ou utilisé Linux (ou bien vous avez tenté, ou ça vous fait peur), on va donc bien tout détailler.

Le terme [Linux](https://www.kernel.org/linux.html) désigne en fait [un noyau de système d'exploitation](https://fr.wikipedia.org/wiki/Noyau_de_système_d%27exploitation). L'équivalent de Windows serait plutôt le terme "distribution GNU/Linux", il y en [des tas](distrowatch.com)&nbsp;! On parle de GNU/Linux car ces systèmes d'exploitation utilisent le noyau Linux et des outils [GNU](https://www.gnu.org/home.fr.html). <!-- TEASER_END -->

Ce guide se focalisera sur l'installation de **[Linux Mint 19 Tara](https://linuxmint.com)**, une distribution parfaite pour débuter sur le monde de Linux&nbsp;!

# Grandes étapes
1. [Préliminaire](#preliminaire)
2. [Préparation de l'installation](#preparation)
3. [Installation de Linux Mint](#installation)

# Préliminaire <a name="preliminaire"></a>

## Récupérer l'image d'installation

La première chose à faire est de récupérer [l'image d'installation de Linux Mint](https://linuxmint.com/download.php). Vous pouvez voir qu'il y a trois éditions disponibles&nbsp;: "Cinnamon", "Xfce" et "MATE". Ces trois éditions viennent avec trois environnements de bureau (des habillages graphiques) différents. La meilleure expérience sera apportée par Cinnamon, car cet environnement de bureau est développé par Linux Mint. MATE est adapté pour les petites configurations et Xfce est un autre bureau assez répandu dans le monde de Linux.

Pour savoir si vous devez installer la version 64-bit ou 32-bit, rendez-vous dans **Panneaux de Configuration > Système et Sécurité > Système**. Il sera indiqué alors si vous avez un processeur 64 bits ou 32 bits.

La suite du tutoriel concernera l'installation de l'édition Cinnamon.

## Création d'une clé USB amorçable

Une clé USB amorçable est simplement une clé USB sur laquelle l'ordinateur peut démarrer. En effet, l'installation de Linux Mint ne se fait pas à partir de Windows, mais à partir d'un mini-système (en l'occurrence Linux Mint) qui sera installé sur la clé. Ce mini système vous permettra également d'avoir un aperçu du système d'exploitation que vous allez installer.

Pour créer une clé amorçable, nous allons utiliser [Rufus](http://rufus.ie). Dans la section téléchargements, sélectionner le lien écrit en gros et téléchargez Rufus. Insérez une clé USB sur votre ordinateur de minimum 4 Go, puis lancez Rufus. 

<figure class="text-center">
<img src="/assets/img/rufus.jpg"
     alt="Interface de Rufus"
     width="40%" />
    <figcaption>Interface de Rufus</figcaption>
</figure>

Il détectera automatiquement votre clé (Périphérique) et il faudra sélectionner l'image de Linux Mint précédemment téléchargée comme Type de Démarrage. Laissez par défaut tout le reste, puis cliquez en bas sur "Démarrer". Si des boîtes de dialogue s'affichent, cliquez sur "Oui".

## Désactivation du démarrage rapide de Windows

Cette fonctionnalité est connue pour causer des effets indésirables. Allez dans **Panneau de configuration > Matériel et audio > Options d’alimentation > Paramètres système**. Cliquez sur **Modifier les options actuellement non disponibles** et désactivez le démarrage rapide.

## Redémarrage de l'ordinateur

Nous pouvons à présent redémarrer l'ordinateur pour procéder à l'installation&nbsp;! Cependant, on ne veut pas revenir dans Windows. Aller dans le menu démarrer et, tout en laissant appuyé la touche Majuscule de gauche, appuyez sur Redémarrer. **Laissez appuyé Maj jusqu'à arriver à l'écran suivant**.

<figure class="text-center">
    <img src="/assets/img/win10_boot_options.jpg"
        alt="Options de démarrage de Windows 10"
        width="75%" />
    <figcaption>L'écran de démarrage avancé de Windows</figcaption>
</figure>

Sélectionnez "Utilisez un autre périphérique" et sélectionnez votre clé. (Quelque chose comme `UEFI: ... marque de votre clé ...`.)

## Démarrage sur la clé

Vous arrivez sur cet écran de sélection d'options de démarrage.

<figure class="text-center">
    <img src="/assets/img/mint_live_grub.png"
        alt="Grub"
        width="75%" />
    <figcaption>GNU Grub</figcaption>
</figure>

Choisissez la première ligne "Start Linux Mint Cinnamon". Après quelques instants, vous êtes sur le bureau de Linux Mint&nbsp;!

<figure class="text-center">
    <img src="/assets/img/mint_live_desktop.png"
        alt="Bureau de Mint Live"
        width="75%" />
    <figcaption>Le bureau Cinnamon</figcaption>
</figure>

Cependant, Linux Mint n'est pas encore installé, vous voyez là le mini-système installé sur la clé. Nous allons passer à la préparation de l'installation&nbsp;: libérer de l'espace sur votre disque dur pour accueillir Mint.

# Préparation de l'installation de Linux Mint<a name="preparation"></a>

## Partitionnement du disque

Un disque dur est toujours divisé en sections que l'on appelle partitions. Nous allons créer trois partitions qui seront utilisées par Linux Mint. Commençons par lancer l'utilitaire qui va nous permettre de faire notre partitionnement&nbsp;: GParted. Pour cela, rendez-vous dans le menu démarrer en bas à gauche et cherchez GParted. L'interface de Cinnamon est pensée pour ne pas trop vous dépayser de Windows.

Dans GParted, en haut à droite, vous pouvez naviguer sur vos disques. Les disques de votre ordinateur s'appellent `/dev/sda`, `/dev/sdb`, etc. 

### Cas où vous avez un SSD

Si vous avez un SSD, vous pouvez installer le système d'exploitation sur celui-ci et stocker vos fichiers sur le disque dur. Dans ce cas, dans GParted, réduisez un volume d'une quarantaine de Go (on se donne une grande marge, en soit, 20 Go peuvent suffire).

Sélectionnez en haut à droite votre disque SSD. Cliquez sur une partition où il y a suffisamment de place et faites un clic droit puis **Redimensionner/Déplacer**. 

**Attention, ne touchez pas à la partition de point de montage qui comprend `/boot` où aux partitions de récupération. En général, celles-ci ne sont de toute façon pas très grandes.** 

Vous pouvez alors libérer de l'espace, soit en indiquant le nombre de Mo à libérer, soit en redimensionnant à la souris la partition. Une fois que c'est fait, vous pouvez cliquer sur **Redimensionner**.

Par exemple, ici, j'ai une seule partition que je m'apprête à redimensionner.

<figure class="text-center">
    <img src="/assets/img/gparted.png"
        alt="GParted"
        width="65%" />
    <figcaption>Interface de GParted</figcaption>
</figure>

Maintenant, allez dans votre disque dur (changez de disque en haut à droite) et libérez 100 Go.

### Cas où vous n'avez pas de SSD

Libérer 140 Go au lieu de 100 Go sur votre disque dur. Il n'est pas nécessaire de libérer plus d'espace pour vos documents puisque vous pourrez accéder à vos fichiers de Windwos depuis Linux Mint. Cependant, l'inverse ne sera pas possible sans installer de logiciel dédié.

**Si vous voulez supprimer Windows de votre ordinateur, formattez simplement la partition de Windows. Ne formattez pas tout le disque, certaines partitions sont nécessaires, comme la partition de démarrage.**

# Installation de Linux Mint sur votre ordinateur<a name="installation"></a>

Sur le bureau, cliquez sur le CD pour installer Linux Mint. Choisissez la langue française,

<figure class="text-center">
    <img src="/assets/img/mint_install_1.png"
        alt="Installation de Linux Mint"
        width="65%" />
    <figcaption>Choix de la languue</figcaption>
</figure>

Et le clavier français.

<figure class="text-center">
    <img src="/assets/img/mint_install_2.png"
        alt="Installation de Linux Mint"
        width="65%" />
    <figcaption>Choix du clavier</figcaption>
</figure>

Si vous êtes en wifi, vous devez maintenant vous connecter au réseau. Ensuite, acceptez les logiciels tiers pour que Linux Mint parvienne à détecter votre matériel.

<figure class="text-center">
    <img src="/assets/img/mint_install_3.png"
        alt="Installation de Linux Mint"
        width="65%" />
    <figcaption>Installation des pilotes propriétaires</figcaption>
</figure>

Sur l'écran de type d'installation, choisissiez "Autre chose"&nbsp;; on arrive alors au moment délicat&nbsp;: le partitionnement. Nous allons définir trois partitions&nbsp;:

* La partition du système&nbsp;;
* La partition des données/documents&nbsp;;
* Une partition de SWAP, ou partition d'échange qui prend le relais de la mémoire vive (RAM) si elle est remplie.

<figure class="text-center">
    <img src="/assets/img/mint_install_4.png"
        alt="Installation de Linux Mint"
        width="65%" />
    <figcaption>Éditeur de partitions de l'installateur</figcaption>
</figure>

Si vous avez le SSD, cherchez l'espace libre que vous avez créé et double cliquez dessus. Vous avez donc cette boîte de dialogue&nbsp;:

<figure class="text-center">
<img src="/assets/img/mint_install_5.png"
     alt="Installation de Linux Mint"
     width="65%" />
    <figcaption>Création d'une partition</figcaption>
</figure>

Laissez l'espace inchangé, on l'a défini tout à l'heure. Laissez les choix par défaut **Partition primaire** et **Début de cet espace**, utilisez comme **Système de fichiers journalisé ext4** et comme point de montage `/` (un simple slash, trouvable dans le menu déroulant). Puis **Ok**. Si vous n'avez pas de SSD prenez 40 Go de votre espace libre du disque dur. L'espace libre a été remplacé pour une nouvelle ligne&nbsp;:

<figure class="text-center">
<img src="/assets/img/mint_install_6.png"
     alt="Installation de Linux Mint"
     width="65%" />
    <figcaption>Une nouvelle partition a été créée</figcaption>
</figure>

Sur le disque dur, sélectionnez votre espace disque et faites une partition de la taille de votre RAM en système de fichiers SWAP. Puis avec ce qui reste, faites une partition ext4 avec pour point de montage `/home`. Toutes les partitions sont **primaires**.

<figure class="text-center">
<img src="/assets/img/mint_install_7.png"
     alt="Installation de Linux Mint"
     width="65%" />
    <figcaption>Exemple de partitions créées</figcaption>
</figure>

**NB.** Cette capture ne représente pas ce que vous devriez avoir. Il s'agit d'un pur exemple. Vous devriez voir aussi apparaître votre premier disque SSD si vous en avez un.

* une partition ext4 `/`&nbsp;;
* une partition ext4 `/home`&nbsp;;
* une partition swap. (En fait Linux Mint n'a pas forcément besoin d'un espace d'échange swap mais en vue d'une installation éventuelle d'un autre système, mieux vaut le faire tout de suite.)

Dans l'écran suivant, vous renseignez votre fuseau horaire et enfin, vous définissez un compte utilisateur. Vous pouvez choisir de crypter vos données et de vous connecter automatiquement au démarrage si vous le souhaitez.

Une fois cela fait, l'installation démarre. Une fois que celle-ci est terminée, vous devrez redémarrer l'ordinateur. Au prochain redémarrage, si vous voyez Grub vous proposer de démarrer sur Linux Mint ou Windows, c'est que l'installation est réussie&nbsp;! En choisissant Linux Mint, vous arrivez sur un écran de connexion. Après avoir entré votre mot de passe, Linux Mint vous accueille sur le bureau Cinnamon.

<figure class="text-center">
<img src="/assets/img/mint_welcome.png"
     alt="Mint Welcome"
     width="65%" />
    <figcaption>Écran de bienvenue de Linux Mint</figcaption>
</figure>

# Et maintenant ?

Je prévois d'écrire un article "Prise en main". Laissez-vous guider par l'écran d'accueil, il vous permettra de bien prendre en main le système et vous pourrez installer vos premiers logiciels. Vous pouvez déjà naviguer sur Internet avec Firefox.