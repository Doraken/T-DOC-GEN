import tkinter as tk
import sys
sys.path.append('../lib/')  # Ajustez selon le chemin réel vers votre dossier lib
from tkinter import simpledialog
from docx import Document
from tableaux_chapitre1 import CreateurTableau  # Assurez-vous que ce module est correctement importé
import json

def load_config():
    config_path = '../config/config.json'  # Chemin vers le fichier de configuration
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def generer_contenu(document, app_name, app_code, config):
    # Utiliser CreateurTableau pour ajouter des tableaux spécifiques au document
    createur = CreateurTableau(document)
    
    # Exemple d'ajout d'un tableau, vous pouvez adapter les entêtes et les lignes comme nécessaire
    entetes = ["Nom de l'Application", "Code Unique"]
    lignes = [[app_name, app_code]]
    createur.ajouter_tableau(entetes, lignes)

def ask_user_info():
    root = tk.Tk()
    root.withdraw()
    app_name = simpledialog.askstring("Nom de l'Application", "Entrez le nom de l'application:", parent=root)
    app_code = simpledialog.askstring("Code Unique", "Entrez le code unique de l'application:", parent=root)
    root.destroy()
    return app_name, app_code

if __name__ == "__main__":
    config = load_config()
    app_name, app_code = ask_user_info()
    if app_name and app_code:
        document = Document()
        generer_contenu(document, app_name, app_code, config)
        save_path = config.get('save_path', './') + f'{app_name}_{app_code}.docx'
        document.save(save_path)
        print(f"Document enregistré : {save_path}")
    else:
        print("Aucune information fournie.")
