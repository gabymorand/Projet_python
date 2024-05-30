# Projet Python: Documentation Automatique, Gestion de Logs et Jeu du Pendu

Bienvenue dans notre projet Python ! Ce projet comprend plusieurs fonctionnalités intéressantes, notamment un jeu de pendu, un programme de gestion de classe, une gestion de log, et une documentation générée automatiquement via Sphinx.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
  - [Jeu du Pendu](#jeu-du-pendu)
  - [Programme de Gestion de Classe](#programme-de-gestion-de-classe)
  - [Gestion de Log](#gestion-de-log)
  - [Documentation Auto via Sphinx](#documentation-auto-via-sphinx)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fonctionnalités

### Jeu du Pendu

Le jeu du pendu est un classique où l'utilisateur doit deviner un mot en proposant des lettres, avec un nombre limité d'essais. Ce programme se trouve dans le fichier `ex01.py`.

### Programme de Gestion de Classe

Ce programme permet de gérer une classe, notamment en calculant la moyenne des élèves, en ajoutant ou supprimant des élèves, et en affichant diverses statistiques. Ce programme se trouve dans le fichier `ex02.py`.

### Gestion de Log

La fonctionnalité de gestion de log permet de suivre les actions et les événements dans le programme. Les logs sont enregistrés dans des fichiers pour une analyse ultérieure. Ce programme se trouve dans le fichier `ex03_log.py`.

### Documentation Auto via Sphinx

La documentation du projet est générée automatiquement à l'aide de Sphinx. Cela permet de maintenir une documentation à jour et facile à naviguer pour les développeurs et les utilisateurs.

## Installation

Pour installer ce projet, suivez les étapes suivantes :

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/gabymorand/Projet_python-docauto-gestionlog-collection-list.git
   cd Projet_python-docauto-gestionlog-collection-list
   ```
## Créez un environnement virtuel et activez-le :

```bash
Copier le code
python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
```
## Installez les dépendances :

```bash
Copier le code
pip install -r requirements.txt
```
Utilisation
## Jeu du Pendu :

Pour lancer le jeu du pendu, exécutez le script ex01.py :

```bash
Copier le code
python ex01.py
```
## Programme de Gestion de Classe :

Pour utiliser le programme de gestion de classe, exécutez le script ex02.py :

```bash
Copier le code
python ex02.py
```
## Gestion de Log :

Pour utiliser la fonctionnalité de gestion de log, exécutez le script ex03_log.py :

```bash
Copier le code
python ex03_log.py
```
## Documentation Auto via Sphinx :

Pour générer la documentation, allez dans le répertoire docs et exécutez :

```bash
Copier le code
make html
```
La documentation sera disponible dans le répertoire _build/html.

##  Contribuer
Les contributions sont les bienvenues ! Pour contribuer :

##  Forkez le projet
Créez votre branche de fonctionnalité (git checkout -b feature/ma-fonctionnalite)
Commitez vos modifications (git commit -am 'Ajout de ma fonctionnalité')
Poussez votre branche (git push origin feature/ma-fonctionnalite)
Ouvrez une Pull Request
##  Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
