# Guide d'édition des barèmes IPP

Ce document vous guide étape par étape pour l'édition des barèmes IPP.
 
- [Étape 1 : Retrouver le fichier YAML du paramètre à modifier](#1-retrouver-le-fichier-YAML-du-paramètre-à-modifier) 
- [Étape 2 : Modifier un paramètre](#2-modifier-le-paramètre)
- [Étape 3 : Enregistrer la modification (Commit)](#3-enregistrer-la-modification-commit) 
- [Étape 4 : Ajouter la modification aux barèmes IPP officiels (Merge Request)](#4-ajouter-la-modification-aux-barèmes-IPP-officiels-merge-request) 
- [FAQ](#foire-aux-questions)


## Étape 1. Retrouver le fichier YAML du paramètre à modifier

- Les barèmes IPP sont visibles par tous [sur le site de l'IPP](https://french-tax-and-benefit-tables.frama.io/baremes-ipp-yaml/).
En vous rendant sur ce site, vous pouvez naviguer dans l'arbre des paramètres législatifs jusqu'à atteindre le paramètre recherché. 

- Sur la page du paramètre recherché, cliquez sur le lien <kbd>Edit</kbd> situé sous le paramètre que vous souhaitez modifier. 
Vous êtes alors automatiquement redirigé vers le [dépôt (_repository_) Git "baremes-ipp-yaml"](https://framagit.org/french-tax-and-benefit-tables/baremes-ipp-yaml) 
au niveau du fichier YAML contenant le paramètre idoine.

Le format [YAML](https://fr.wikipedia.org/wiki/YAML) est le format retenu pour les paramètres législatifs d'[OpenFisca](https://openfisca.org/doc/coding-the-legislation/legislation_parameters.html).
Il permet de représenter de façon lisible des informations élaborées comme une combinaison de listes et de dictionnaires imbriqués.
Il est nécessaire de bien respecter:
- l'indentation introduisant les sous-structures,
- les tirets `-` marquers des listes
- les deux points séparant les clés des valeurs dans un dictionnaire 

## Étape 2. Modifier le paramètre

Avant de modifier les barèmes IPP pour la première fois, 
il convient de lire [**les règles d'édition**](https://framagit.org/french-tax-and-benefit-tables/ipp-tax-and-benefit-tables-xlsx/blob/master/guide_legislation.md) 
des paramètres législatifs.

Pour modifier le fichier YAML, cliquez sur le bouton <kbd>Edit</kbd> situé dans le coin supérieur droit de la page.

#### Option 1 : Modifier/corriger un paramètre existant

- Structure
  - Chaque fichier YAML peut regrouper un ou plusieurs paramètres en plus d'une description et de méta-données
    - La champ `description` servira de titre à la table où à la colonne rassemblant les valeurs des paramètres qu'elle contient (les lignes étant des dates).
    - Le champ `metadata` peut contenir les champs suivants qui viendront s'ajouter aux colonnes 
      - `order`: indique l'ordre dans lequel sont rangés les paramètres
      - `reference`: les références législatives classées par date
      - `date_parution_au_jo`: les dates de parution au Journal officiel classées par date
      - `note`: : les dates de parution au Journal officiel classées par date

  - Chaque paramètre dispose également d'une `description` et de méta-données (`metadata`)
    - La champ `description` servira de nom au paramètre
    - Le champ `metadata` décrira ceratines caractéristiques des paramètres qu'il s'agira de respecter lors de l'édition de ses valeurs 

- Marche à suivre
  - Dans le champs `values` du paramètre, ajoutez la nouvelle valeur du paramètre et la date de début correspondante (ou corrigez la valeur, le cas échéant).
  - Dans le champs `reference` de `metadata`, ajoutez la référence législative justifiant votre changement.
  - Dans le champs `date_parution_jo` de `metadata`, ajoutez la date de parution au Journal officiel de la référence.

- Exemple
  Je souhaite mettre à jour la valeur du plafond de la Sécurité Sociale pour 2019. 
  Pour l'instant, les barèmes IPP s'arrêtent en 2018. Je rajoute sa nouvelle valeur qui prend effet à partir du 1er janvier 2019 et la référence législative.
  
  *NB : cet exemple est entièrement fictif.*
 
  ```diff
   plafond_securite_sociale_annuel:
   description: Plafond de la Sécurité sociale (annuel)
   values:
  +  2019-01-01:
  +    value: 50000.0
     2018-01-01:
      value: 39732.0 
  ```
  ```diff
   metadata:
     order:
       - plafond_securite_sociale_mensuel
       - plafond_securite_sociale_annuel
     reference:
  +   2019-01-01: Arrêté du 03/12/2018
      2018-01-01: Arrêté du 05/12/2017
      2017-01-01: Arrêté du 05/12/2016
      [...]
     date_parution_jo:
  +   2019-01-01: 2018-12-13
      2018-01-01: 2017-12-09
  ```
    
#### Option 2 : Ajouter un nouveau paramètre dans un fichier YAML

- Marche à suivre
  - Ajoutez le nom de votre paramètre : en tout attaché, sans majuscules, sans espaces (utillisez des tirets du bas `_` comme séparateur si nécessaire)
  - Ajoutez un champs `description`
  - Ajoutez un champs `values`
  - Ajoutez un champs `metadata` avec deux sous-champs : `ipp_csv_id` et `unit`.
     - Les unités possibles pour les paramètres sont des nombres sans unités (``/1``) comme des taux ou des nombres d'enfants, des valeurs monétaires (``currency-EUR`` ou ``currency-FRF``) ou des années (``year``)
     - Le champ `ipp_csv_id` correspond simplement au nom du paramètre pour export vers la version Stata de TAXIPP. Il convient donc de lui donner un nom compréhensible mais court (moins de 32 caractères car c'est la limite dans Stata).
  - Identifiez visuellement la place de votre nouveau paramètre dans le barème (c'est important pour la visualisation sur le site de l'IPP)
    Il y a souvent plusieurs paramètres par fichier YAML, et il peut aussi y avoir plusieurs sous-sections par fichiers YAML. Il faut donc choisir la manière dont ils s'affichent.
  - Dans la section déjà existante `order` de `metadata` du fichier YAML, ajoutez le nom de votre paramètre (insérez-le à l'endroit choisi)

 - Exemple
   Je souhaite ajouter le paramètre de taux de dégressivité de la prime d'activité (PPA). 
   
   *NB : cet exemple est fictif, ce paramètre existe déjà.*

    ```diff
    + majoration_ressources_revenus_activite:
    +   description: Majoration des ressources sur les revenus d'activité
    +   values:
    +     2016-01-01:
    +       value: 0.62
    +   metadata:
    +     ipp_csv_id: pa_maj_revenu
    +     unit: /1
    ```
    ```diff
    metadata:
    order:
     - majoration_montant_maximal_en_base_rsa
     - majoration_isolement_en_base_rsa
    + - majoration_ressources_revenus_activite
     - bonification
     - montant_minimum_verse
    reference:
    ```

#### Option 3 : Créer un nouveau fichier YAML

TODO à rédiger
   
## Étape 3. Enregistrer la modification (COMMIT)

Une fois que vous avez modifié le barème dans l'éditeur en ligne, 
il est nécessaire de *"commiter"* ce changement sinon il ne sera pas enregistré.

- Entrez un message de commit dans la case <kbd>Commit message</kbd> en bas de votre éditeur (cf .[les règles d'écriture d'un message de commit utile](https://chris.beams.io/posts/git-commit/)).
- Entrez le nom de la branche sur laquelle vous souhaitez effectuer le commit, dans la case <kbd>Target branch</kbd> (donnez lui un nom qui a un sens !)
- Cochez la case <kbd>Start a new merge request with these changes</kbd>

Pour les débutants : [quelque rappels sur Git et le version control](https://framagit.org/ipp/ipp-survival-gitbook/blob/master/git.md)

## Étape 4. Ajouter la modification aux barèmes IPP publiés (MERGE REQUEST)

Si vous avez demandé l'ouverture d'une Merge Request, vous êtes automatiquement redirigé vers la page de cette Merge Request.
Pour rappel, une Merge Request est une opération qui vise à fusionner les modifications que vous avez effectuées sur votre branche dans une autre branche (généralement la branche principale `master`).
Ici la branche "source" est votre branche personnelle sur laquelle vous avez modifié les barèmes et la branche "target" est la branche `master`.

- Donnez un titre à votre Merge Request : ce titre doit décrire en 1 ligne l'ensemble des changements effectués (soyez concis)
- Dans la description, décrivez plus en détail chaque changement, avec éventuellement des liens vers vos références etc.
Vous pouvez retrouver tout en bas de la page, la liste des commits que vous avez faits sur votre branche. En cliquant dessus, vous pouvez visualiser les changements introduits.
- Finalisez votre Merge Request en cliquant sur <kbd>Submit merge request</kbd>. Vous pourrez toujours la modifier par la suite en cliquant sur le bouton <kbd>Edit</kbd>.

## Foire aux questions

- [Je ne peux pas éditer le fichier YAML sur le dépôt Git "baremes-ipp-yaml"](#je-ne-peux-pas-editer-le-fichier-yaml-sur-le-dépot-git-baremes-ipp-yaml) 
- [Je souhaite faire plusieurs modifications groupées / J'ai oublié d'ajouter quelque chose](#je-souhaite-faire-plusieurs-modifications-groupées-j-ai-oublié-d-ajouter-quelque-chose) 
- [Je souhaite annuler mes modifications](#je-souhaite-annuler-mes-modifications)


### Je ne peux pas éditer le fichier YAML sur le dépôt Git `baremes-ipp-yaml`

Afin de pouvoir éditer, il faut être membre du projet *baremes-ipp-yaml* et avoir un 
statut au moins équivalent à celui de "Developper" pour avoir des droits d'édition. 
Demandez à être rajouté par [un des membres autorisé ("Owner")](https://framagit.org/french-tax-and-benefit-tables/baremes-ipp-yaml/project_members) à le faire.

### Je souhaite faire plusieurs modifications groupées / J'ai oublié d'ajouter quelque chose

Il est possible de faire plusieurs petites modifications des barèmes (commits) et de les grouper ensemble dans une seule Merge Request.  
Dans ce cas, ne cochez pas la case <kbd>Start a new merge request with these changes</kbd> lors de vos commits (étape 3).
Vous pouvez effectuer plusieurs commits sur la même branche (c'est-à-dire répéter les étapes 2 et 3). 

Une fois que vous avez fini, vous pouvez vous rendre sur la page ["branches"](https://framagit.org/french-tax-and-benefit-tables/baremes-ipp-yaml/branches)
pour retrouver votre branche et cliquer sur le bouton <kbd>Merge Request</kbd>.

Même une fois la Merge Request ouverte, il est possible de continuer à faire des commits sur votre branche si vous avez oublié de modifier quelque chose.

NB : Une Merge Request doit, autant que possible, introduire un groupe de changements cohérents.

- Exemple 1 : 

  Le gouvernement annonce une revalorisation exceptionelle des prestations sociales de 10%.
  Je modifie le barème du montant de base du RSA (1 commit), puis de la prime d'activité (1 commit) puis des APL (1 commit)  
  Je fais donc une seule Merge Request avec tous ces commits.

- Exemple 2 : 

  Le PLF 2019 introduit une revalorisation de l'ASPA et une augmentation de la taxation indirecte.
  Je fais donc deux Merge Request distinctes.

### Je souhaite annuler mes modifications

- Si vous vous rendez compte de votre erreur avant d'avoir fait votre commit, pas de soucis, le changement n'a pas été pris en compte.
- Si vous vous rendez compte de votre erreur après avoir fait le commit mais avant de merger, pas de soucis, il suffit de faire un nouveau commit qui corrige votre erreur.
- Si vous vous rendez compte de votre erreur après que vos changement aient été mergés (c'est-à-dire qu'ils ont été incorporés au barèmes IPP officiels, dans la branche `master`)
  alors il faut créer au plus vite une nouvelle branche avec un commit qui corrige votre erreur et créer une nouvelle merge request.
