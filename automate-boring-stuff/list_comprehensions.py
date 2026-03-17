import os, unicodedata

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
#1
#----- [EXPRESSION for VARIABLE in ITERABLE]
numbers = [1, 2, 3, 4, 5]
doubles = [n * 2 for n in numbers]

names = ["Alice", "hans", "JoEL"]
upper = [name.upper() for name in names]

words = ["chat", "chien", "oiseau"]
lengths = [len(word) for word in words]

strings = ["42", "18", "7"]
numbers = [int(s) for s in strings]

#2
# ----- [EXPRESSION for VARIABLE in ITERABLE if CONDITION]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]

#3- Generator expressions
# ----- (EXPRESSION for VARIABLE in ITERABLE if CONDITION)
# This is a generator expression, which creates an iterator that generates the values on demand instead of storing them all in memory at once.

#4 - Dict comprehensions
# ----- {KEY_EXPRESSION: VALUE_EXPRESSION for VARIABLE in ITERABLE if CONDITION}

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
# -> {1: 'a', 2: 'b', 3: 'c'}

# Filter a dictionary
scores = {"Alice": 85, "Bob": 45, "Dave": 38}
passed = {name: score for name, score in scores.items() if score >= 50}
# -> {'Alice': 85}

# initialize un compteur
categories = ["images", "documents", "music"]
summary = {cat: 0 for cat in categories}
# -> {"images": 0, "documents": 0, "music": 0}

#5 - comprehensions inmbriquées
# ----- [EXPRESSION for VARIABLE in ITERABLE for VARIABLE2 in ITERABLE2 if CONDITION]
# boucles
result = []
for row in range(1, 4):
    for col in range(1, 4):
        result.append(row * col)
# -> [1, 2, 3, 2, 4, 6, 3, 6, 9]

# Equivalent list comprehension
result = [row * col for row in range(1, 4) for col in range(1, 4)]

# 8 - Exo
#8.1 - rewrite these code using list comprehensions
# a) extract extensions
files = ["report.pdf", "photo.jpg", "data.csv", "notes.txt", "image.png"]
extensions = []
for f in files:
    extensions.append(os.path.splitext(f)[1])

extensions_comp = [os.path.splitext(f)[1] for f in files]

#b) keep only positive numbers
numbers = [4, -2, 7, -5, 0, 3, -1, 8]
positives = []
for n in numbers:
    if n > 0:
        positives.append(n)

positives_comp = [n for n in numbers if n > 0]

#c) create a dict {filename: size} for the files in a folder
sizes = {}
for f in os.listdir(desktop):
    filepath = os.path.join(desktop, f)
    if os.path.isfile(filepath):
        sizes[f] = os.path.getsize(filepath)

sizes_comp = {
    f: os.path.getsize(os.path.join(desktop, f))
    for f in os.listdir(desktop)
    if os.path.isfile(os.path.join(desktop, f))
}

# 8.2 - rewrite the function remove_accents

def remove_accents(text):
    """Remove accents from a string."""

    return "".join(t for t in unicodedata.normalize("NFD", text) if unicodedata.category(t) != "Mn")

# 8.3 - write a function summarize_folder(folder) that returns a dict with the count of files by extension in the given folder.
def summarize_folder(folder):
    # 1 - get all extensions
    extensions = [
        os.path.splitext(f)[1].lower()
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]

    #2 - count the occurrences of each extension
    counts = {}
    for ext in extensions:
        counts.setdefault(ext, 0)
        counts[ext] += 1
    
    return counts