import os
import json

def update_config_paths():
    # Obtenir le chemin absolu du répertoire parent de bin/ (racine du projet)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Chemin vers le fichier de configuration
    config_path = os.path.join(project_root, 'config', 'config.json')

    # Charger la configuration existante si elle existe, sinon créer une nouvelle
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
    else:
        config = {}

    # Mettre à jour les chemins dans la configuration avec le chemin racine en premier
    config['chemin_racine'] = project_root.replace("\\", "/")  # Utiliser des chemins POSIX
    # Mise à jour des chemins pour lib et run en utilisant le chemin racine
    config['chemin_lib'] = os.path.join(config['chemin_racine'], 'lib/').replace("\\", "/")
    config['chemin_run'] = os.path.join(config['chemin_racine'], 'run/').replace("\\", "/")
    config['chemin_log_base'] = os.path.join(config['chemin_racine'], 'data/log/').replace("\\", "/")
    config['data_directories'] = {
        'resources': os.path.join(config['chemin_racine'], 'data/resources').replace("\\", "/"),
        'import_templates': os.path.join(config['chemin_racine'], 'data/resources/import_templates').replace("\\", "/"),
        'images': os.path.join(config['chemin_racine'], 'data/resources/images').replace("\\", "/")
    }

    # Écrire la configuration mise à jour dans le fichier
    with open(config_path, 'w') as file:
        json.dump(config, file, indent=4, ensure_ascii=False)

    print("Les chemins de configuration ont été mis à jour.")

if __name__ == "__main__":
    update_config_paths()
