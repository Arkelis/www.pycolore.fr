---
title: Indiquer à Git la clé SSH à utiliser pour les opérations avec les dépôts distants
slug: indiquer-a-git-la-cle-ssh-a-utiliser-pour-les-operations-avec-les-depots-distants
date: 2020-12-26 16:40:12 UTC+01:00
tags: Git
category: Mémo
link: 
description: 
type: text
---

On peut être amené à avoir plusieurs clés SSH sur un même ordinateur. Si on interagit avec les dépots distants (par exemple sur Github ou Gitlab) en SSH, il faut s'assurer que Git utilise une clé qui est enregistrée sur le compte. <!-- TEASER_END -->

Pour ce faire, on peut utiliser la configuration `core.sshCommand`, typiquement :

```bash
git config core.sshCommand "ssh -i ~/.ssh/fichier-cle-privee"
```

Git utilisera alors cette commande pour toutes les interactions qui utilisent SSH, comme on y spécifie la clé que l'on veut, on est sûr que la bonne clé sera utilisée. Cette configuration est spécifique à chaque dépôt local.
