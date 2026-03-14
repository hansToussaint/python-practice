import pdfplumber, logging, os, re

#2
files = ["data1.pdf", "data2.pdf", "NOTEXIST.pdf", "data4.pdf", "data5.pdf"]

for f in files:
    try:
        with pdfplumber.open(f) as pdf:
            text = pdf.pages[0].extract_text()
            print(f"OK: {f}")
    except:
        print(f"Error: {f}")

#3 - Catch specific error!!
"""
try:
    result = int(user_input)
except ValueError:
    print("This is not a number")
"""

#Current errors
"""
# FileNotFoundError — fichier introuvable
open("inexistant.txt")

# ValueError — mauvaise valeur
int("abc")

# KeyError — clé inexistante dans un dict
d = {"a": 1}
d["b"]

# TypeError — mauvais type
"hello" + 5

# IndexError — index hors limites
liste = [1, 2, 3]
liste[10]

# ZeroDivisionError — division par zéro
10 / 0

# PermissionError — pas le droit d'accéder
open(r"C:\Windows\system32\config\sam")

# AttributeError — méthode qui n'existe pas
"hello".inexistant()
"""

# catch multiples error
"""
try:
    data = process_file(filepath)
except FileNotFoundError:
    print(f"File {filepath} not found")
except ValueError:
    print(f"invalid data in {filepath}")
except PermissionError:
    print(f"You do not have permission to read {filepath}")
"""

#4
try:
    result = int("acb")
except ValueError as e:
    print(f"Error: {e}")
    # → "Error: invalid literal for int() with base 10: 'abc'"

# Exception catch almost all errors
# except Exception as e:

#6 - try/except/else/finally
"""
try:
    f = open("data.txt", "r")
    text = f.read()
except FileNotFoundError:
    print("Fichier introuvable!")
else:
    # S'exécute SEULEMENT si PAS d'erreur
    print(f"Fichier lu: {len(text)} caractères")
finally:
    # S'exécute TOUJOURS, erreur ou pas
    print("Terminé")
"""

#7 - 2 ways. python prefer EAFP
"""
# LBYL — "Look Before You Leap" (vérifie avant)
if os.path.exists(filepath):
    with open(filepath) as f:
        text = f.read()
else:
    print("Fichier introuvable")

# EAFP — "Easier to Ask Forgiveness than Permission" (essaie d'abord)
try:
    with open(filepath) as f:
        text = f.read()
except FileNotFoundError:
    print("Fichier introuvable")
"""
# python prefer EAFP
# Parce que entre le moment où tu vérifies et le moment où tu agis, quelque chose peut changer.
"""
# Race condition possible
if os.path.exists("data.txt"):          # fichier existe...
    # ...un autre programme le supprime ici...
    with open("data.txt") as f:         # CRASH!
        text = f.read()
"""

#9
#9.1 - write a function safe_read_pdf

def safe_read_pdf(pdf_path, logger):
    """Read a pdf securely. return the text or None if error."""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    except FileNotFoundError:
        logger.error("pdf not found")
        return None
    except Exception as e:
        logger.error(f"Error: {e}")
        return None
    else:
        return text

# log
def setup_logging():
    logger = logging.getLogger("my_safe_function")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H-%M-%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

logger = setup_logging()

safe_read_pdf("no.pdf", logger)

#9.2 - write a script that never crash
files = [
    "rapport.pdf",           # existe
    "inexistant.pdf",        # n'existe pas
    "notes.txt",             # existe mais pas un PDF
    "data.pdf",              # existe
    "corrompu.pdf",          # existe mais corrompu
]

def process_file(filepath, logger):
    """Treat a file. Return (True, text) or (False, reason)."""

    # verification 1: the file exists?
    if not os.path.exists(filepath):
        return False, "File not found"

    # 2: Is the file a pdf?
    if not filepath.lower().endswith(".pdf"):
        return False, "Not a pdf"

    #3: Can we read it?
    try:
        with pdfplumber.open(filepath) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return True, text
    except Exception as e:
        return False, f"Error reading..: {e}"

def main():
    logger=setup_logging()
    logger.info("---Session started---")

    success = 0
    failed = []

    for filepath in files:
        ok, result = process_file(filepath, logger)

        if ok:
            logger.info(f"{filepath}: OK ({len(result)} caratères)")
            success += 1
        else:
            logger.error(f"{filepath}: {result}")
            failed.append(filepath)
        
    logger.info(f"---Session ended | Success: {success} | Failed: {len(failed)} ---")

#9.3
text = """
Numéro: FAC-2024-0892
Date: 15 mars 2024
TOTAL: 384.60$
"""

patterns = {
    "invoice": r"FAC-\d{4}-\d{4}",
    "date": r"\d{1,2}\s+\w+\s+\d{4}",
    "total": r"TOTAL:\s*(\d+\.\d+)",
    "phone": r"\(\d{3}\)\s*\d{3}-\d{4}",    # pas dans le texte!
}

def safe_extract(text, patterns, logger):
    """Extract data with regex"""

    results = {}

    for name, pattern in patterns.items():
        try:
            match = re.search(pattern, text)
            if match:
                # if the pattern has a group, take group(1), else group(0)
                results[name] = match.group(1) if match.lastindex else match.group(0)
            else:
                results[name] = None
                logger.warning(f"'{name}' not found")
        except Exception as e:
            results[name] = None
            logger.error(f"Invalid regex for '{name}': {e}")
            
    return results

result = safe_extract(text, patterns, logger)
print(result)
# → {"invoice": "FAC-2024-0892", "date": "15 mars 2024", "total": "384.60", "phone": None}
