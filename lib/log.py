# log.py

from datetime import datetime
import os
import json

class Log:
    def __init__(self):
        self.fichier_log = None
        # Charger le chemin de base et le chemin des logs depuis le fichier de configuration
        self.configurations = self.load_config()
        self.chemin_log_base = self.configurations['chemin_log_base']

    def load_config(self):
        # Calculer le chemin absolu vers le fichier de configuration en utilisant chemin_racine
        dir_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(dir_path, '..', 'config', 'config.json')
        with open(config_path, 'r') as fichier:
            configurations = json.load(fichier)
        return configurations

    def open(self):
        if not self.fichier_log:
            format_nom_fichier = "execution_%Y-%m-%d-%H-%M-%S.log"
            nom_fichier_log = datetime.now().strftime(format_nom_fichier)
            chemin_complet_log = os.path.join(self.configurations['chemin_racine'], self.chemin_log_base, nom_fichier_log)
            # S'assurer que le répertoire existe
            os.makedirs(os.path.dirname(chemin_complet_log), exist_ok=True)
            self.fichier_log = open(chemin_complet_log, 'a')
    
    def write_line(self, message):
        if self.fichier_log:
            format_horodatage = "[%d/%m/%Y - %Hh%Mm%Ss] - "
            message_horodate = datetime.now().strftime(format_horodatage) + message + "\n"
            self.fichier_log.write(message_horodate)
    
    def close(self):
        if self.fichier_log:
            self.fichier_log.close()
            self.fichier_log = None
