# T-DOC-GEN
Technical DOCumentation GENerator

# Projet de Scripting Python

Ce projet contient une collection de scripts Python destinés à automatiser la création de documents Word et à gérer des scénarios d'exécution spécifiques à travers une interface graphique.

## Description

Le projet vise à faciliter la génération automatique de fichiers Word basés sur les entrées utilisateur et à fournir un mécanisme pour exécuter divers scénarios d'application. Il comprend également un système de logging personnalisé pour enregistrer les actions de l'utilisateur et les événements d'exécution.

### Fonctionnalités

- Interface graphique pour saisir le nom de l'application et le code du projet.
- Génération automatique de fichiers Word contenant des informations spécifiées par l'utilisateur.
- Logging des actions et des événements dans des fichiers spécifiques.
- Possibilité d'exécuter différents scénarios d'application à partir d'une interface graphique.

## Commencer

### Prérequis

- Python 3.6 ou supérieur
- Bibliothèques Python : `tkinter` et `python-docx`

### Installation

Clonez le dépôt sur votre machine locale :

```bash
git clone https://github.com/Doraken/T-DOC-GEN

### Structure du Projet

Le projet est structuré comme suit :

projet/
│
├── bin/
│   ├── launcher.py  # Script pour lancer l'application
│   └── configure_paths.py  # Script pour configurer les chemins
│
├── config/
│   └── config.json  # Fichier de configuration des chemins
│
├── lib/
│   └── log.py  # Module de logging personnalisé
│
├── run/
│   └── scenario_base.py  # Script de scénario de base
│
└── data/
    ├── log/  # Répertoire pour les fichiers de log
    └── output/  # Répertoire pour les fichiers Word générés


## Utilisation

Pour lancer l'application, exécutez le script `launcher.py` situé dans le dossier `bin/` :

```bash
python bin/launcher.py
