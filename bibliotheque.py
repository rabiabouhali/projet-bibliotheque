import json
import os

# Chemin du fichier JSON
FICHIER_JSON = 'bibliotheque.json'


# Fonction pour charger la bibliothèque depuis le fichier JSON


def charger_bibliotheque():
    if os.path.exists(FICHIER_JSON):
        with open(FICHIER_JSON, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


# Fonction pour sauvegarder la bibliothèque dans le fichier JSON


def sauvegarder_bibliotheque(bibliotheque):
    with open(FICHIER_JSON, 'w') as f:
        json.dump(bibliotheque, f, indent=4)


# Fonction pour ajouter un livre


def ajouter_livre(bibliotheque):
    """Ajoute un nouveau livre à la bibliothèque."""
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    try:
        annee = int(input("Entrez l'année de publication : "))
    except ValueError:
        print("Année invalide. Le livre n'a pas été ajouté.")
        return

    # Générer un ID unique
    nouvel_id = max([livre['ID'] for livre in bibliotheque], default=0) + 1

    # Créer le nouveau livre
    nouveau_livre = {
        "ID": nouvel_id,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None
    }

    # Ajouter le livre à la bibliothèque
    bibliotheque.append(nouveau_livre)
    print("Livre ajouté avec succès !")


# Fonction principale


def main():
    print("Bienvenue dans la bibliothèque personnelle de Rabia Bouhali")
    bibliotheque = charger_bibliotheque()
    # Boucle principale du menu
    while True:
        print("\n1. Afficher tous les livres")
        print("2. Ajouter un livre")
        print("3. Supprimer un livre")
        print("4. Rechercher un livre")
        print("5. Marquer un livre comme lu")
        print("6. Trier les livres")
        print("7. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "7":
            sauvegarder_bibliotheque(bibliotheque)
            print("Bibliothèque sauvegardée. Au revoir !")
            break
        else:
            print("Fonctionnalité non implémentée")


def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("Aucun livre dans la bibliothèque.")
        return
    for livre in bibliotheque:
        statut = "Lu" if livre["Lu"] else "Non lu"
        print(f"\nID: {livre['ID']}")
        print(f"Titre: {livre['Titre']}")
        print(f"Auteur: {livre['Auteur']}")
        print(f"Année: {livre['Année']}")
        print(f"Statut: {statut}")
        if livre["Note"] is not None:
            print(f"Note: {livre['Note']}/10")


if __name__ == "__main__":
    main()
