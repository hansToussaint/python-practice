import unicodedata, re

# 2 - les majuscules
text = "Accepté"
text.upper()    # → "ACCEPTÉ"
text.lower()    # → "accepté"

# 3 - Les accents

text = "é"
decomposed = unicodedata.normalize("NFD", text)
print(len(text))           # → 1 (un caractère)
print(len(decomposed))     # → 2 (e + accent séparé)


text = "Destoné"
# Étape 1 : décomposer
decomposed = unicodedata.normalize("NFD", text)
# "Destoné" → "D e s t o n e ́"  (l'accent est séparé)

# Étape 2 : garder seulement les caractères qui ne sont PAS des accents
clean = ""
for char in decomposed:
    if unicodedata.category(char) != "Mn":
        clean += char

print(clean)    # → "Destone"  (accent enlevé!)

"""
unicodedata.category("D")    # → "Lu"  (Letter, uppercase)
unicodedata.category("e")    # → "Ll"  (Letter, lowercase)
unicodedata.category("5")    # → "Nd"  (Number, digit)
unicodedata.category(" ")    # → "Zs"  (Separator, space)

# Et le fameux :
unicodedata.category("́")     # → "Mn"  (Mark, nonspacing) ← C'EST UN ACCENT!
"""

#6
"""
import unicodedata

# Nom d'un caractère
unicodedata.name("é")     # → 'LATIN SMALL LETTER E WITH ACUTE'
unicodedata.name("ç")     # → 'LATIN SMALL LETTER C WITH CEDILLA'
unicodedata.name("€")     # → 'EURO SIGN'

# Trouver un caractère par son nom
unicodedata.lookup("EURO SIGN")     # → '€'

# Catégorie
unicodedata.category("A")     # → 'Lu' (Letter, uppercase)
unicodedata.category("a")     # → 'Ll' (Letter, lowercase)
unicodedata.category("1")     # → 'Nd' (Number, decimal digit)
unicodedata.category("!")     # → 'Po' (Punctuation, other)
"""

#7
#7.1 - normalize

def normalize(text):
    # security
    if text is None:
        return ""
    
    #all to str then in lower
    text_str = str(text)
    text_lower = text_str.lower()

    #encoding
    decomposed = unicodedata.normalize("NFD", text_lower)
    
    clean = ""
    for char in decomposed:
        if unicodedata.category(char) != "Mn":
            clean += char

    # keep only letters
    result = re.sub(r"[^a-z0-9]", "", clean)

    return result

# Tous ces cas doivent donner le même résultat
assert normalize("Café") == normalize("cafe") == normalize("CAFÉ") == normalize("C.A F.É")
assert normalize("Québec!") == normalize("quebec") == normalize("QUEBEC")
assert normalize("micro-ondes") == normalize("micrOondes") == normalize("MICRO ONDES")
assert normalize(None) == ""
assert normalize(12345) == "12345"
print("Tous les tests passent!")

# 7.2
lots = [
    "20260216-BB03 Destoné",
    "20260216-BB04 Micro-ondes",
    "20260216-BB05 Nature",
]
"""
result = find_match("20260216-bb03 destone", lots)
print(result)    # → "20260216-BB03 Destoné"

result = find_match("20260216-bb04 microondes", lots)
print(result)    # → "20260216-BB04 Micro-ondes"

result = find_match("20260216-BB99 Inexistant", lots)
print(result)    # → None
"""
def find_match(target, candidates):
    for candidate in candidates:
        if normalize(target) == normalize(candidate):
            return candidate
    
    return None

# 7.3
def remove_accents(text):
    #security
    if text is None:
        return ""

    #encoding
    decomposed = unicodedata.normalize("NFD", text_lower)

    clean = ""
    for char in decomposed:
        if unicodedata.category(char) != "Mn":
            clean += char

    return clean
