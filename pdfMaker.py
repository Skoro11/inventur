import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

data = [
    ("Früchtecocktail", "Gemüse & Obst", "Dose"),
    ("Ananas", "Gemüse & Obst", "Dose"),
    ("Pfirsiche", "Gemüse & Obst", "Dose"),
    ("Mohren", "Gemüse & Obst", "Kg"),
    ("Ajvar", "Gewürze & Saucen", "Glass"),
    ("Zucker", "Gewürze & Saucen", "Kg"),
    ("Mais", "Gemüse & Obst", "Dose"),
    ("Kartoffeln", "Gemüse & Obst", "Kg"),
    ("Essig", "Gemüse & Obst", "Liter"),
    ("Vegeta", "Gewürze & Saucen", "Kg"),
    ("Salz", "Gewürze & Saucen", "Kg"),
    ("Reis", "Getreide, Nudeln & Reis", "Kg"),
    ("Paniermehl", "Getreide, Nudeln & Reis", "Kg"),
    ("Bandnudeln", "Getreide, Nudeln & Reis", "Kg"),
    ("Pommes Frites", "Tiefkühlprodukte", "Kg"),
    ("Rösti", "Tiefkühlprodukte", "Kg"),
    ("Kroketten", "Tiefkühlprodukte", "Kg"),
    ("Brokkoli", "Tiefkühlprodukte", "Kg"),
    ("Blumenkohl", "Gemüse & Obst", "Kg"),
    ("Rote Bete", "Gemüse & Obst", "Dose"),
    ("Gemüse", "Tiefkühlprodukte", "Kg"),
    ("Mehl", "Getreide, Nudeln & Reis", "Kg"),
    ("Tomaten", "Gemüse & Obst", "Kg"),
    ("Gurken", "Gemüse & Obst", "Stück"),
    ("Champignons", "Gemüse & Obst", "Kg"),
    ("Orangen", "Gemüse & Obst", "Stück"),
    ("Zitronen", "Gemüse & Obst", "Stück"),
    ("Petersilie", "Gemüse & Obst", "Bund"),
    ("Eisbergsalat", "Gemüse & Obst", "Kopfe"),
    ("Eier", "Milchprodukte & Eier", "Stück"),
    ("French Dressing", "Gewürze & Saucen", "Liter"),
    ("Oliven", "Gewürze & Saucen", "Dose"),
    ("Kraut", "Gewürze & Saucen", "Kopf"),
    ("Joghurt", "Milchprodukte & Eier", "Kg"),
    ("H-Sahne", "Milchprodukte & Eier", "Liter"),
    ("Hollandaise", "Gewürze & Saucen", "Liter"),
    ("Bernaise", "Gewürze & Saucen", "Liter"),
    ("Käse", "Milchprodukte & Eier", "Kg"),
    ("Butter", "Milchprodukte & Eier", "Stück"),
    ("Himbeersauce", "Gewürze & Saucen", "Liter"),
    ("Eis Schokolade", "Tiefkühlprodukte", "Liter"),
    ("Eis Vanille", "Tiefkühlprodukte", "Liter"),
    ("Zigeunerschnitzelsauce", "Gewürze & Saucen", "Kg"),
    ("Schokosauce", "Gewürze & Saucen", "Liter"),
    ("Milch", "Milchprodukte & Eier", "Liter"),
    ("Camembert", "Milchprodukte & Eier", "Stück"),
    ("Kräuterbutter", "Getreide, Nudeln & Reis", "grams"),
    ("Schnecken", "Fleisch & Meeresfrüchte", ""),
    ("Grüner Pfeffer", "Gewürze & Saucen", "Dose"),
    ("Senf", "Gewürze & Saucen", ""),
    ("Bernaisepulver", "Gewürze & Saucen", ""),
    ("Rahmsaucepulver", "Gewürze & Saucen", "Kg"),
    ("Portion Mayonnaise", "Gewürze & Saucen", ""),
    ("Portion Ketchup", "Gewürze & Saucen", ""),
    ("Tiefgekühlte Himbeeren", "Tiefkühlprodukte", "Kg"),
    ("Schattenmorellen", "Tiefkühlprodukte", "Kg"),
    ("Toast", "Getreide, Nudeln & Reis", "Stück"),
    ("Öl", "Sonstige", "Liter"),
    ("Schweinefilet", "Fleisch & Meeresfrüchte", "Kg"),
    ("Schweinelachse", "Fleisch & Meeresfrüchte", "Kg"),
    ("Rumpsteak", "Fleisch & Meeresfrüchte", "Kg"),
    ("Putensteak", "Fleisch & Meeresfrüchte", "Kg"),
    ("Kaffeesahne", "Milchprodukte & Eier", "Liter"),
    ("Portion Zucker", "Gewürze & Saucen", "Kg"),
    ("Bohnenkaffee", "Getränke (Nicht-alkoholisch)", "Kg"),
    ("Plavac", "Weine", "Liter"),
    ("Pelješac", "Weine", "Liter"),
    ("Dalmatiner", "Weine", "Liter"),
    ("Graševina", "Weine", "Liter"),
    ("Laški Riesling", "Weine", "Liter"),
    ("Traminac", "Weine", "Liter"),
    ("Rosé", "Weine", "Liter"),
    ("Cola Light", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Cola", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Fanta", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Sprite", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Apfelschorle", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Orangensaft", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Bitter Lemon", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Malzbier", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Alkoholfreies Bier", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Weizen alkoholfrei", "Biere", "Kiste"),
    ("Bier Gaffel", "Biere", "Fass 50Liter"),
    ("Krombacher", "Biere", "Fass 50Liter"),
    ("Malteser", "Getränke (Alkoholisch)", "Flasche"),
    ("Landbier", "Biere", "Fass 30Liter"),
    ("Weizen Fass", "Biere", "Fass 30Liter"),
    ("Sekt", "Getränke (Alkoholisch)", "Flasche"),
    ("Campari", "Getränke (Alkoholisch)", "Flasche"),
    ("Korn", "Getränke (Alkoholisch)", "Flasche"),
    ("Ramazzotti", "Getränke (Alkoholisch)", "Flasche"),
    ("Jägermeister", "Getränke (Alkoholisch)", "Flasche"),
    ("Kruškovac", "Getränke (Alkoholisch)", "Liter"),
    ("Šljivovica", "Getränke (Alkoholisch)", "Liter"),
    ("Wodka", "Getränke (Alkoholisch)", "Flasche"),
    ("Tequila", "Getränke (Alkoholisch)", "Flasche"),
    ("Ouzo", "Getränke (Alkoholisch)", "Flasche"),
    ("Jubi", "Getränke (Alkoholisch)", "Flasche"),
    ("Kabanes", "Getränke (Alkoholisch)", "Flasche"),
    ("Grappa", "Getränke (Alkoholisch)", "Flasche"),
    ("Williamsbirne", "Getränke (Alkoholisch)", "Flasche"),
    ("Amaretto", "Getränke (Alkoholisch)", "Flasche"),
    ("Jim Beam", "Getränke (Alkoholisch)", "Flasche"),
    ("Sambuca", "Getränke (Alkoholisch)", "Flasche"),
    ("Rum", "Getränke (Alkoholisch)", "Flasche"),
    ("Baileys", "Getränke (Alkoholisch)", "Flasche"),
    ("Pelinkovac", "Getränke (Alkoholisch)", "Flasche"),
    ("Linie", "Getränke (Alkoholisch)", "Flasche"),
    ("Orahovac", "Getränke (Alkoholisch)", "Flasche"),
    ("Bauchspeck", "Fleisch & Meeresfrüchte", "Kg"),
    ("Garnelle", "Fleisch & Meeresfrüchte", "Kg"),
    ("Zander", "Fleisch & Meeresfrüchte", "Kg"),
    ("Krabben", "Fleisch & Meeresfrüchte", "Kg"),
    ("Lachsfille", "Fleisch & Meeresfrüchte", "Kg"),
    ("Kirschsaft", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Bananensaft", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Rhababerschorle", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Johannisbeereschorle", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Wasser 0,25", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Stilwasser 0,25", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Wasser 0,7", "Getränke (Nicht-alkoholisch)", "Kiste"),
    ("Pflanzenfett", "Sonstige", "Liter"),
    ("Erdbeereis", "Tiefkühlprodukte", "Liter")
]


# Convert to DataFrame and sort by category and item (alphabetically within each category)
df = pd.DataFrame(data, columns=["Artikel", "Kategorie", "Menge"])
df = df.sort_values(by=["Kategorie", "Artikel"])  # Sort by category and then alphabetically by item

# PDF file name
pdf_file = "restaurant_inventory.pdf"
pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

# Initialize table data with headers
table_data = [["Artikel", "Menge", "Preis"]]

# Retrieve unique categories
categories = df["Kategorie"].unique()

# Loop through categories and add items to the table
category_indices = []  # List to track category rows for styling
for category in categories:
    table_data.append([category, "", ""])  # Add category row
    category_indices.append(len(table_data) - 1)  # Store the index of the category row
    
    # Add item rows for this category
    category_rows = df[df["Kategorie"] == category].apply(lambda x: [x["Artikel"], x["Menge"], ""], axis=1).tolist()
    table_data.extend(category_rows)
    
    # Add two empty rows for spacing between categories
    table_data.append(["", "", ""])  # Empty row for spacing
    table_data.append(["", "", ""])  # Another empty row for spacing

# Table Styling
table = Table(table_data, colWidths=[200, 100, 100])
style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 0), (-1, -1), 8)
])

# Right-align the "Menge" column (index 1)
style.add("ALIGN", (1, 1), (-1, -1), "RIGHT")

# Style category rows
for i in category_indices:
    style.add("SPAN", (0, i), (-1, i))  # Span the whole row for the category
    style.add("BACKGROUND", (0, i), (-1, i), colors.lightgrey)  # Light grey background for category row
    style.add("ALIGN", (0, i), (-1, i), "CENTER")  # Center-align the category row

table.setStyle(style)

# Build and save the PDF
pdf.build([table])

print(f"PDF saved as {pdf_file}")
