import os
import re # Nécessaire pour gérer le gras (**text**) et le code (`text`)

# On force Python à travailler dans le dossier du script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def md_to_html(input_md, output_html):
    try:
        if not os.path.exists(input_md):
            print(f"Erreur : {input_md} introuvable.")
            return

        with open(input_md, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        html_content = ""
        in_table = False
        in_list = False

        for line in lines:
            line = line.strip()

            # 1. Conversion du formatage Markdown (Gras et Code)
            # Remplace **texte** par <strong>texte</strong>
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            # Remplace `texte` par <code>texte</code> (pour les IP)
            line = re.sub(r'`(.*?)`', r'<code style="background-color: #f8f9fa; padding: 2px 4px; border-radius: 4px; color: #d63384;">\1</code>', line)

            # 2. Gestion des fins de blocs (Tableaux et Listes)
            if in_table and "|" not in line:
                html_content += "</table>\n"
                in_table = False
            
            if in_list and not line.startswith("- "):
                html_content += "</ul>\n"
                in_list = False

            # 3. Traitement des lignes
            
            # Titres
            if line.startswith("# "):
                html_content += f"<h1 class='mt-4 mb-3'>{line[2:]}</h1>\n"
            elif line.startswith("## "):
                html_content += f"<h2 class='mt-4 mb-3 border-bottom pb-2'>{line[3:]}</h2>\n"
            
            # Listes à puces
            elif line.startswith("- "):
                if not in_list:
                    html_content += "<ul>\n"
                    in_list = True
                html_content += f"<li>{line[2:]}</li>\n"
            
            # Tableaux
            elif "|" in line:
                if "---" in line: # Ignorer la ligne de séparation Markdown
                    continue
                
                if not in_table:
                    html_content += '<div class="table-responsive"><table class="table table-striped table-hover table-bordered">\n'
                    in_table = True
                    is_header = True # La première ligne trouvée est l'en-tête
                else:
                    is_header = False

                cells = line.split("|")[1:-1]
                
                if is_header:
                    row = "".join([f"<th class='table-dark'>{c.strip()}</th>" for c in cells])
                    html_content += f"<thead><tr>{row}</tr></thead><tbody>\n"
                else:
                    row = "".join([f"<td>{c.strip()}</td>" for c in cells])
                    html_content += f"<tr>{row}</tr>\n"
            
            # Citations / Blockquotes (Context)
            elif line.startswith("> "):
                html_content += f"<div class='alert alert-info'>{line[2:]}</div>\n"

            # Paragraphes simples (seulement si la ligne n'est pas vide)
            elif line:
                html_content += f"<p>{line}</p>\n"

        # Fermeture des blocs résiduels si le fichier finit brusquement
        if in_table: html_content += "</tbody></table></div>\n"
        if in_list: html_content += "</ul>\n"

        # 4. Structure HTML Finale (Bootstrap 5)
        full_page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Rapport de Sécurité Réseau</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #f0f2f5; padding-top: 20px; padding-bottom: 50px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        .container {{ max-width: 1000px; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }}
        h1 {{ color: #1a73e8; font-weight: 700; }}
        h2 {{ color: #2c3e50; font-size: 1.5rem; }}
        li {{ margin-bottom: 8px; }}
        strong {{ color: #dc3545; }} /* Met le texte gras (alertes) en rouge */
    </style>
</head>
<body>
    <div class="container">
        {html_content}
        <footer class="text-center text-muted mt-5 pt-3 border-top">
            <small>Généré automatiquement par Python Script (SAE 1.05)</small>
        </footer>
    </div>
</body>
</html>"""

        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(full_page)

        print(f"✅ Succès ! Rapport généré : {output_html}")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    md_to_html('Network_Report.md', 'Network_Report.html')