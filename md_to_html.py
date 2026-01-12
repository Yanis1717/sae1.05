import os

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

        for line in lines:
            line = line.strip()

            # Gestion des titres
            if line.startswith("# "):
                html_content += f"<h1>{line[2:]}</h1>\n"
            elif line.startswith("## "):
                html_content += f"<h2>{line[3:]}</h2>\n"
            
            # Gestion des listes (puces)
            elif line.startswith("- "):
                html_content += f"<li>{line[2:]}</li>\n"
            
            # Gestion simplifiée des tableaux
            elif "|" in line:
                if not in_table:
                    html_content += '<table class="table table-striped">\n'
                    in_table = True
                if ":---" in line: # On saute la ligne de séparation du MD
                    continue
                cells = line.split("|")[1:-1]
                tag = "th" if "Timestamp" in line or "Source" in line else "td"
                row = "".join([f"<{tag}>{c.strip()}</{tag}>" for c in cells])
                html_content += f"<tr>{row}</tr>\n"
            
            else:
                if in_table:
                    html_content += "</table>\n"
                    in_table = False
                if line:
                    html_content += f"<p>{line}</p>\n"

        # Structure finale avec Bootstrap (chargé via internet ou utilisable en local)
        full_page = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Rapport de Sécurité</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{ padding: 50px; background: #f4f4f4; font-family: sans-serif; }}
        .report {{ background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #0d6efd; }}
        h2 {{ color: #444; margin-top: 25px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background: #f8f9fa; }}
    </style>
</head>
<body>
    <div class="container report">
        {html_content}
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