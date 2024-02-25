import os
import json
from pathlib import Path
from importlib import import_module

def charger_configurations():
    config_file = Path(__file__).parent.parent / 'config' / 'config.json'
    with open(config_file, 'r') as fichier:
        return json.load(fichier)

configurations = charger_configurations()

def generer_fichiers_config():
    templates_path = Path(configurations['chemin_racine']) / configurations['data_directories']['import_templates']
    config_dir = Path(configurations['chemin_racine']) / 'config'
    
    config_dir.mkdir(parents=True, exist_ok=True)
    
    for filename in os.listdir(templates_path):
        if filename.endswith('.docx'):
            type_doc = filename.split('_')[0]
            config_filename = f'config_{type_doc}.json'
            config_path = config_dir / config_filename
            config_content = {
                "type": type_doc,
                "description": f"Configuration for {type_doc} documents"
            }
            with open(config_path, 'w') as config_file:
                json.dump(config_content, config_file, indent=4)
            print(f"Generated config file: {config_path}")

if __name__ == "__main__":
    generer_fichiers_config()
