# L'évolution de barèmes IPP 

## Un bref historique

### Barèmes au format Excel sans versionnement

La première version des barèmes IPP étaient une collection de fichiers Excel hébergés sur le serveur local de l'IPP.  

Ce choix est la conséquence des constations suivantes: 
- Excel est l'outil "populaire" en édition et consommation
- Exposés sur le site de l'IPP idoine

Par ailleurs, ces fichiers Excel étaient consommés par la version de TAXIPP en Stata.

### Barèmes au format Excel versionné

Afin de conserver l'outil "populaire" mais d'introduire un minimum de gestion de version, il a été décidé de créer un dépôt Git.
Un seul dépôt local a été partagé par tous les membres (non sans heurts) et synchronisé avec le dépôt distant (framagit).

### Barèmes au format Excel versionné et parsé

Les fichiers Excel .(xls, .xlsx) sont des fichiers binaires qui ne peuvent pas être comparés facilement (le _diff_ est illisible).
Il a donc été décidé de réaliser moulinettes permmattant: 
- la production automatique de fichiers YAML lisisbles par les utilisateurs
- la production automatique de fichiers csv pour TAXIPP en stata

Ce fût une première étape pour injecter les paramètres dans OpenFisca/TAXIPP en Python.

## Problèmes non résolus

### Unicité du dépôt local

- Il n'existe qu'un seul dépôt à l'IPP modifié par tous les membres. Ce n'est pas vraiment pratique surtout si l'on est sur plusieurs bureaux.

### Le _diff_  reste largement illisible 

Le Excel est illisible, il faut aller vérifier les fichiers YAML produits. Ce qui est rarement fait par les contributeurs car compliqué. 

### La chaîne de production reste assez fragile et trop complexe

- L'édition des fichiers Excel n'est pas assez contraignante
- La validation est compliquée
- La maintenance des différents scripts n'est pas simple et introduit de la fragilité


### La fusion avec openfisca n'a pas aboutie

- Elle a été largement entamé
- Mais elle reste compliquée et elle n'est pas terminée

### Contributions extérieurs

- Il n'y a pas de capitalisation sur les  contributions extérieures
- Le traitement des signalements extérieurs sont traités manuellement


## Objectifs poursuivis par la nouvelle organisation

1. Versionnement sur [ce dépôt](https://framagit.org/french-tax-and-benefit-tables/baremes-ipp-yaml) 

2. Exposition de [pages générées à la volée sur le site web de l'IPP](https://french-tax-and-benefit-tables.frama.io/baremes-ipp-yaml/) via [ces scripts](https://github.com/fpagnoux/baremes-ipp-views) 

3. Production automatique des fichiers [`csv`](https://github.com/fpagnoux/baremes-ipp-csv) pour TAXIPP en Stata via [ce script](https://github.com/fpagnoux/baremes-ipp-parser/tree/master/bareme_ipp_parsers)

4. Alimenter une base unique utilisée aussi pour [OpenFisca](https://github.com/openfisca/openfisca-france)/TAXIPP en Python

5. Valider les contributions internes et externes
