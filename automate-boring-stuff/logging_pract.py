import logging

#2
"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Ceci est un debug")
logging.info("Ceci est une info")
logging.warning("Ceci est un warning")
logging.error("Ceci est une erreur")
"""

#4 - professional log
# a. create a logger named
logger = logging.getLogger("mon_script")
logger.setLevel(logging.DEBUG)

# b. format
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
#the code above define the format
#2024-03-15 14:30:22 | INFO     | File succesfully uploaded
#2024-03-15 14:30:23 | ERROR    | PDF illisible!

# c. create Handlers
    # write in file
file_handler = logging.FileHandler("script.log", mode="a", encoding="utf-8")
file_handler.setFormatter(formatter)

    # print to terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# d. connect handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#5 - all in one function
def setup_logging(log_file="script.log"):
    """
    setup the logging to write in file and in the terminal
    Return the logger ready to use
    """

    logger = logging.getLogger("my_script")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # file (permanent)
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Terminal (real time)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# How to use it:
"""
logger = setup_logging("mon_script.log")

logger.info("Script démarré")
logger.info("Traitement de fichier1.pdf")
logger.warning("Colonne 'COA#' introuvable")
logger.error("fichier2.pdf est illisible")
logger.info("Script terminé")
```

**Dans le terminal ET dans `mon_script.log` :**
```
2024-03-15 14:30:22 | INFO     | Script démarré
2024-03-15 14:30:22 | INFO     | Traitement de fichier1.pdf
2024-03-15 14:30:23 | WARNING  | Colonne 'COA#' introuvable
2024-03-15 14:30:24 | ERROR    | fichier2.pdf est illisible
2024-03-15 14:30:24 | INFO     | Script terminé
"""

#6 pass the logger to functions
"""
# ❌ Logger global — ça marche mais c'est moins propre
def find_row(ws, lot_id):
    logging.info("Recherche...")

# ✅ Logger en paramètre — plus explicite, testable
def find_row(ws, lot_id, logger):
    logger.info("Recherche...")
"""

#7 - different levels by handler
def setup_logging_level(log_file="script.log"):
    logger = logging.getLogger("my_script")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s"
        datefmt = "%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
