import csv

def generer_markdown():
    # On lit le CSV déjà généré par le 1er programme
    with open("Donnee_Reseau.csv", "r", encoding="utf-8-sig") as f:
        lecteur = csv.reader(f, delimiter=';')
        lignes = list(lecteur)

    # La première ligne = en-têtes
    entetes = lignes[0]
    donnees = lignes[1:]  # toutes les lignes de paquets

    # On crée le fichier Markdown
    with open("rapport_reseau.md", "w", encoding="utf-8") as md:
        # Titre
        md.write("# Analyse du trafic réseau (site Inde)\n\n")
        
        # Nombre total de paquets
        md.write(f"Nombre total de paquets analysés : **{len(donnees)}**\n\n")

        # Aperçu des 50 premières lignes
        md.write("## Aperçu des 50 premiers paquets\n\n")
        for ligne in donnees[:50]:
            heure, source, dest, info = ligne
            md.write(f"- {heure} ; {source} ; {dest} ; {info}\n")
        md.write("\n")

        # Exemple de paquets HTTP
        md.write("## Exemple de paquets HTTP\n\n")
        compteur_http = 0
        for ligne in donnees:
            heure, source, dest, info = ligne
            if "HTTP" in info and compteur_http < 5:
                md.write(f"- {heure} ; {source} ; {dest} ; {info}\n")
                compteur_http += 1

        if compteur_http == 0:
            md.write("_Aucun paquet HTTP détecté dans cet extrait._\n")

if __name__ == "__main__":
    generer_markdown()
    print("rapport_reseau.md généré.")