from docx import Document

class CreateurTableau:
    def __init__(self, document: Document):
        self.document = document

    def ajouter_tableau(self, entetes: list, lignes: list):
        """
        Ajoute un tableau au document avec les entêtes et les lignes spécifiées.

        :param entetes: Liste des en-têtes de colonnes du tableau.
        :param lignes: Liste de listes, chaque sous-liste correspondant à une ligne du tableau.
        """
        if not entetes or not lignes:
            print("Les entêtes et les lignes sont nécessaires pour créer un tableau.")
            return

        # Créer le tableau dans le document avec le nombre de lignes et de colonnes approprié
        tableau = self.document.add_table(rows=1, cols=len(entetes))
        
        # Configurer le style du tableau (optionnel)
        tableau.style = 'Table Grid'

        # Remplir l'en-tête du tableau
        for idx, en_tete in enumerate(entetes):
            tableau.rows[0].cells[idx].text = en_tete

        # Ajouter les données dans le tableau
        for ligne in lignes:
            cells = tableau.add_row().cells
            for idx, cellule in enumerate(ligne):
                cells[idx].text = str(cellule)

# Exemple d'utilisation
if __name__ == "__main__":
    doc = Document()
    createur = CreateurTableau(doc)
    entetes = ["En-tête 1", "En-tête 2", "En-tête 3"]
    lignes = [
        ["Ligne 1, Cellule 1", "Ligne 1, Cellule 2", "Ligne 1, Cellule 3"],
        ["Ligne 2, Cellule 1", "Ligne 2, Cellule 2", "Ligne 2, Cellule 3"],
    ]
    createur.ajouter_tableau(entetes, lignes)
    doc.save("exemple_tableau.docx")
