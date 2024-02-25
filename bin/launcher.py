import os
import sys
import json
from importlib import import_module
import tkinter as tk

# Ajouter le répertoire `run/` à sys.path
chemin_run = os.path.join(os.path.dirname(__file__), '..', 'run')
if chemin_run not in sys.path:
    sys.path.append(chemin_run)

# Charger les configurations depuis le fichier config.json
def charger_configurations():
    config_file = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    with open(config_file, 'r') as fichier:
        return json.load(fichier)

configurations = charger_configurations()

# Ajouter le répertoire `lib/` au PYTHONPATH pour pouvoir importer log
sys.path.append(os.path.join(os.path.dirname(__file__), '..', configurations['chemin_lib']))
from log import Log

# Fonction pour lister les scénarios disponibles
def lister_scenarios():
    return [f[:-3] for f in os.listdir(chemin_run) if f.endswith('.py') and not f.startswith('__')]

# Fonction pour exécuter un scénario spécifique
def executer_scenario(nom_scenario):
    try:
        # Importer le module du scénario spécifique
        scenario_module = import_module(nom_scenario)
        scenario_module.run()
    except ImportError as e:
        print(f"Erreur lors de l'importation du scénario {nom_scenario}: {e}")
    except AttributeError:
        print(f"Le scénario {nom_scenario} n'a pas de fonction 'run()'.")

# Fonction pour afficher le menu graphique et sélectionner un scénario
def afficher_menu_graphique(scenarios):
    def on_select():
        index = liste_scenarios.curselection()[0]
        scenario_selectionne = scenarios[index]
        fenetre.destroy()
        executer_scenario(scenario_selectionne)

    fenetre = tk.Tk()
    fenetre.title("Sélection du scénario")
    tk.Label(fenetre, text="Sélectionnez un scénario à exécuter :").pack()

    liste_scenarios = tk.Listbox(fenetre)
    for scenario in scenarios:
        liste_scenarios.insert(tk.END, scenario)
    liste_scenarios.pack()

    bouton_executer = tk.Button(fenetre, text="Exécuter", command=on_select)
    bouton_executer.pack()

    fenetre.mainloop()

if __name__ == "__main__":
    log = Log()
    log.open()
    log.write_line("Démarrage du launcher")

    scenarios = lister_scenarios()
    if scenarios:
        afficher_menu_graphique(scenarios)

    log.write_line("Fin de l'exécution du launcher")
    log.close()
