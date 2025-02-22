import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Data provided (formatted into a structured list)
data = [
    ("Früchtecocktail", "Gemüse & Obst"),
    ("Ananas", "Gemüse & Obst"),
    ("Pfirsiche", "Gemüse & Obst"),
    ("Mohren", "Gemüse & Obst"),
    ("Ajvar", "Gewürze & Saucen"),
    ("Zucker", "Gewürze & Saucen"),
    ("Mais", "Gemüse & Obst"),
    ("Kartoffeln", "Gemüse & Obst"),
    ("Essig", "Gemüse & Obst"),
    ("Vegeta", "Gewürze & Saucen"),
    ("Salz", "Gewürze & Saucen"),
    ("Reis", "Getreide, Nudeln & Reis"),
    ("Paniermehl", "Getreide, Nudeln & Reis"),
    ("Bandnudeln", "Getreide, Nudeln & Reis"),
    ("Pommes Frites", "Tiefkühlprodukte"),
    ("Rösti", "Tiefkühlprodukte"),
    ("Kroketten", "Tiefkühlprodukte"),
    ("Rote Bete", "Gemüse & Obst"),
    ("Brokkoli", "Gemüse & Obst"),
    ("Blumenkohl", "Gemüse & Obst"),
    ("Gemüse", "Gemüse & Obst"),
    ("Mehl", "Getreide, Nudeln & Reis"),
    ("Tomaten", "Gemüse & Obst"),
    ("Gurken", "Gemüse & Obst"),
    ("Champignons", "Gemüse & Obst"),
    ("Orangen", "Gemüse & Obst"),
    ("Zitronen", "Gemüse & Obst"),
    ("Petersilie", "Gemüse & Obst"),
    ("Eisbergsalat", "Gemüse & Obst"),
    ("Eier", "Milchprodukte & Eier"),
    ("French Dressing", "Gewürze & Saucen"),
    ("Oliven", "Gewürze & Saucen"),
    ("Krautsalat", "Gewürze & Saucen"),
    ("Joghurt", "Milchprodukte & Eier"),
    ("H-Sahne", "Milchprodukte & Eier"),
    ("Hollandaise", "Gewürze & Saucen"),
    ("Bernaise", "Gewürze & Saucen"),
    ("Käse", "Milchprodukte & Eier"),
    ("Butter", "Milchprodukte & Eier"),
    ("Himbeersauce", "Gewürze & Saucen"),
    ("Eis Schokolade", "Tiefkühlprodukte"),
    ("Eis Vanille", "Tiefkühlprodukte"),
    ("Zigeunerschnitzelsauce", "Gewürze & Saucen"),
    ("Schokosauce", "Gewürze & Saucen"),
    ("Milch", "Milchprodukte & Eier"),
    ("Camembert", "Milchprodukte & Eier"),
    ("Kräuterbutter", "Milchprodukte & Eier"),
    ("Schnecken", "Fleisch & Meeresfrüchte"),
    ("Grüner Pfeffer", "Gewürze & Saucen"),
    ("Senf", "Gewürze & Saucen"),
    ("Bernaisepulver", "Gewürze & Saucen"),
    ("Rahmsaucepulver", "Gewürze & Saucen"),
    ("Portion Mayonnaise", "Gewürze & Saucen"),
    ("Portion Ketchup", "Gewürze & Saucen"),
    ("Tiefgekühlte Himbeeren", "Tiefkühlprodukte"),
    ("Schattenmorellen", "Tiefkühlprodukte"),
    ("Toast", "Getreide, Nudeln & Reis"),
    ("Öl", "Sonstige"),
    ("Schweinefilet", "Fleisch & Meeresfrüchte"),
    ("Schweinelachse", "Fleisch & Meeresfrüchte"),
    ("Rumpsteak", "Fleisch & Meeresfrüchte"),
    ("Putensteak", "Fleisch & Meeresfrüchte"),
    ("Kaffeesahne", "Milchprodukte & Eier"),
    ("Portion Zucker", "Gewürze & Saucen"),
    ("Bohnenkaffee", "Getränke (Nicht-alkoholisch)"),
    ("Plavac", "Weine"),
    ("Pelješac", "Weine"),
    ("Dalmatiner", "Weine"),
    ("Graševina", "Weine"),
    ("Laški Riesling", "Weine"),
    ("Traminac", "Weine"),
    ("Rosé", "Weine"),
    ("Cola Light", "Getränke (Nicht-alkoholisch)"),
    ("Cola", "Getränke (Nicht-alkoholisch)"),
    ("Fanta", "Getränke (Nicht-alkoholisch)"),
    ("Sprite", "Getränke (Nicht-alkoholisch)"),
    ("Wasser", "Getränke (Nicht-alkoholisch)"),
    ("Apfelschorle", "Getränke (Nicht-alkoholisch)"),
    ("Orangensaft", "Getränke (Nicht-alkoholisch)"),
    ("Bitter Lemon", "Getränke (Nicht-alkoholisch)"),
    ("Malzbier", "Getränke (Nicht-alkoholisch)"),
    ("Alkoholfreies Bier", "Getränke (Nicht-alkoholisch)"),
    ("Weizenbier", "Biere"),
    ("Bier Gaffel", "Biere"),
    ("Krombacher", "Biere"),
    ("Malteser", "Getränke (Alkoholisch)"),
    ("Landbier", "Biere"),
    ("Weizen Fass", "Biere"),
    ("Sekt", "Getränke (Alkoholisch)"),
    ("Campari", "Getränke (Alkoholisch)"),
    ("Korn", "Getränke (Alkoholisch)"),
    ("Ramazzotti", "Getränke (Alkoholisch)"),
    ("Jägermeister", "Getränke (Alkoholisch)"),
    ("Kruškovac", "Getränke (Alkoholisch)"),
    ("Šljivovica", "Getränke (Alkoholisch)"),
    ("Pelinkovac", "Getränke (Alkoholisch)"),
    ("Wodka", "Getränke (Alkoholisch)"),
    ("Tequila", "Getränke (Alkoholisch)"),
    ("Ouzo", "Getränke (Alkoholisch)"),
    ("Jubi", "Getränke (Alkoholisch)"),
    ("Kabanes", "Getränke (Alkoholisch)"),
    ("Grappa", "Getränke (Alkoholisch)"),
    ("Williamsbirne", "Getränke (Alkoholisch)"),
    ("Amaretto", "Getränke (Alkoholisch)"),
    ("Jim Beam", "Getränke (Alkoholisch)"),
    ("Sambuca", "Getränke (Alkoholisch)"),
    ("Rum", "Getränke (Alkoholisch)"),
    ("Baileys", "Getränke (Alkoholisch)"),
    ("Pelinkovac", "Getränke (Alkoholisch)"),
    ("Linie", "Getränke (Alkoholisch)"),
    ("Orahovac", "Getränke (Alkoholisch)"),
    ("Erdbeereis", "Tiefkühlprodukte")
];

# Convert to DataFrame and sort
df = pd.DataFrame(data, columns=["Artikel", "Kategorie"])
df = df.sort_values(by="Kategorie")

# PDF file name
pdf_file = "restaurant_inventory.pdf"
pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

# Updated header row
table_data = [["Artikel", "Menge", "Preis"]]  # Updated Headers

categories = df["Kategorie"].unique()
category_indices = []

for category in categories:
    table_data.append([category, "", ""])  # Category row
    category_indices.append(len(table_data) - 1)
    
    category_rows = df[df["Kategorie"] == category].apply(lambda x: [x["Artikel"], "", ""], axis=1).tolist()
    table_data.extend(category_rows)
    table_data.append(["", "", ""])  # Empty row for spacing
    table_data.append(["", "", ""])  # Another empty row for spacing

# Table Styling
table = Table(table_data, colWidths=[200, 100, 100])
style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black)
])

for i in category_indices:
    style.add("SPAN", (0, i), (-1, i))
    style.add("BACKGROUND", (0, i), (-1, i), colors.lightgrey)
    style.add("ALIGN", (0, i), (-1, i), "CENTER")

table.setStyle(style)
pdf.build([table])

print(f"PDF saved as {pdf_file}")
