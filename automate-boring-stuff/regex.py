import re

"""
    # Les bases
    \d        # un chiffre
    \w        # une lettre, chiffre ou _
    \s        # un espace, tab, newline
    .         # n'importe quel caractère SAUF newline
    +         # 1 ou plus
    *         # 0 ou plus
    ?         # 0 ou 1
    {3}       # exactement 3
    {2,5}     # entre 2 et 5

    \W        # tout ce qui n'est PAS \w
    \S        # tout ce qui n'est PAS un espace (pratique!)
    [:\s]+    # ":" et/ou espaces
    .+        # tout le reste de la ligne
    Gourmand vs paresseux (.+ vs .+?)
"""

# 2 - group
#2.1 write a regex that extract name and age from texts below
texts = [
    "Patient: Alice Martin, Age: 34",
    "Patient: Bob Tremblay, Age: 67",
    "Patient: Clara Dubois, Age: 23"
]

for text in texts:
    match = re.search(r"Patient: (.+), Age: (\d+)", text)

    if match:
        name = match.group(1)
        age = match.group(2)
        print(f"{name}, {age}")
        

# 3 - crochets
#3.1 write a func that takes in a phone number in ever format and returns the digits

def clean_phone(phone):
    return re.sub(r"[^0-9]", "", phone)


# 4 - | (OU) et Le groupe non-capturant (?:)
"""
  text = "J'ai 3 chats et 5 chiens"
  m = re.search(r"(\d+) (chats|chiens)", text)
  m = re.search(r"(\d+) (chats|chiens)", text)
  m.group(1)    # → '3'
  m.group(2)    # → 'chats'

  m = re.search(r"(\d+) (?:chats|chiens)", text)
  m.group(1)    # → '3'
  m.group(2)    # → ERREUR! pas de groupe 2


  # Sans (?:) — les groupes sont un désordre
  r"((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)"
  # Groupes: 1=mois, 2=prefix_mois, 3=jour, 4=prefix_jour, 5=année, 6=prefix_année

  # Avec (?:) — propre
  r"((?:0|1)?\d)-((?:0|1|2|3)?\d)-((?:19|20)\d\d)"
  # Groupes: 1=mois, 2=jour, 3=année
"""

#5 - flags

#    re.search(r"salmonella", "Salmonella Negative", re.IGNORECASE)    # → match! (ou re.I)

    # Avec VERBOSE — documenté
#    pattern = re.compile(r"""
#        Salmonell\w*          # "Salmonella" ou "Salmonelle" etc.
#        \s+                   # espace(s)
#        (Negative|Positive)   # résultat (capturé dans groupe 1)
#        \s*/?\s*              # espace optionnel, slash optionnel
#        25\s*g                # "25 g" ou "25g"
#   """, re.VERBOSE | re.IGNORECASE)


#6 - re.search() - find first match vs re.findall() - all matches vs re.finditer()
#6.1

lab_report = """
Sample: ENT-001
Test: Salmonella - Negative /25 g
Test: Coliforms - 49 MPN/g
Test: E.coli - <10 CFU/g

Sample: ENT-002
Test: Salmonella - Positive /25 g
Test: Coliforms - 120 MPN/g
Test: E.coli - 35 CFU/g

Sample: ENT-003
Test: Salmonella - Negative /25 g
Test: Coliforms - 12 MPN/g
Test: E.coli - <10 CFU/g
"""

samples = re.findall(r"ENT-\d{3}", lab_report)

salm_pattern = re.compile(r"""
    Salmonell\w*    # Salmonella or Salmonelle etc
    \s*             # 0 or many spaces
    -
    \s*
    (Negative|Positive)
    \s*/?\s*        # space and slash optional
    25\s*g          # "25 g" ou "25g"
""", re.VERBOSE | re.I)
salm_results = re.findall(salm_pattern, lab_report)

col_results = re.findall(r"Coliforms\s*-\s*(\d+)", lab_report)

print(samples)
print(salm_results)
print(col_results)

# 8
#8.1

invoice = """
FACTURE
Numéro: FAC-2024-0892
Date: 15 mars 2024
Client: Laboratoire Québec Inc.
Adresse: 1401 Ch. de Chambly, Longueuil, QC J4J 3X6

Description                    Quantité    Prix unitaire    Total
Analyse Salmonella             3           45.00$           135.00$
Analyse Coliforms              3           38.50$           115.50$
Analyse E.coli                 2           42.00$           84.00$

Sous-total: 334.50$
TPS (5%): 16.73$
TVQ (9.975%): 33.37$
TOTAL: 384.60$
"""

# Extrais :
# 1. Numéro de facture → "FAC-2024-0892"
# 2. Date → "15 mars 2024"
# 3. Nom du client → "Laboratoire Québec Inc."
# 4. Code postal → "J4J 3X6"
# 5. Le TOTAL → "384.60"
# 6. Tous les noms d'analyses avec findall → ["Salmonella", "Coliforms", "E.coli"]
# 7. Tous les montants de la colonne Total avec findall → ["135.00", "115.50", "84.00"]

invoice_number = re.search(r"FAC-\d{4}-\d{4}", invoice).group()
date = re.search(r"\d{1,2}\s+\w+\s+\d{4}", invoice).group()
client = re.search(r"Client:\s*(.+)", invoice).group(1)
postal_code = re.search(r"[A-Z]\d[A-Z]\s*\d[A-Z]\d", invoice).group()
total = re.search(r"TOTAL:\s*(\d+\.\d+)", invoice).group(1)
analysis = re.findall(r"Analyse\s+([\w\.]+)", invoice)

line_totals = re.findall(r"\d+\.\d+\$\s+(\d+\.\d+)\$", invoice)
# Explication: Tu matches le prix unitaire sans le capturer, puis tu captures le total.
#Comme ça tu ignores automatiquement le sous-total, TPS et TVQ qui n'ont pas un montant avec $ juste avant.
