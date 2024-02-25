import os
import json
from pathlib import Path
from docx import Document

def charger_configurations():
    # Charge les configurations à partir du fichier config.json
    config_file = Path(__file__).parent.parent / 'config' / 'config.json'
    with open(config_file, 'r') as fichier:
        return json.load(fichier)

configurations = charger_configurations()

def extraire_titres(document_path):
    # Extrait les titres et leurs niveaux à partir du document Word (.docx)
    document = Document(document_path)
    titres = []
    for paragraph in document.paragraphs:
        if paragraph.style.name.startswith('Heading'):
            niveau = int(paragraph.style.name[-1])
            titre = paragraph.text
            titres.append((titre, niveau))
    return titres

def creer_structure_hierarchique(titres, document_name):
    # Crée une structure hiérarchique basée sur les titres et leurs niveaux
    structure_hierarchique = {}
    for titre, niveau in titres:
        current_level = structure_hierarchique
        for _ in range(niveau - 1):
            current_level = current_level.setdefault(titre, {})
        current_level[titre] = {}
    return {document_name: structure_hierarchique}

def generer_fichiers_config():
    # Chemin vers le répertoire des modèles d'importation et le répertoire de configuration
    templates_path = Path(configurations['chemin_racine']) / configurations['data_directories']['import_templates']
    config_dir = Path(configurations['chemin_racine']) / 'config'
    
    config_dir.mkdir(parents=True, exist_ok=True)
    
    # Parcours de tous les fichiers dans le répertoire des modèles d'importation
    for filename in os.listdir(templates_path):
        if filename.endswith('.docx'):
            # Récupère le type de document à partir du nom du fichier
            type_doc = filename.split('_')[0]
            # Nom du fichier de configuration à générer
            config_filename = f'config_{type_doc}.json'
            config_path = config_dir / config_filename
            document_path = templates_path / filename
            
            # Extrait les titres du document
            titres = extraire_titres(document_path)
            # Crée la structure hiérarchique des titres
            structure_hierarchique = creer_structure_hierarchique(titres, document_name=type_doc)
            
            # Enregistre la structure hiérarchique dans un fichier JSON
            with open(config_path, 'w') as config_file:
                json.dump(structure_hierarchique, config_file, indent=4)
            print(f"Generated config file: {config_path}")

if __name__ == "__main__":
    generer_fichiers_config()
