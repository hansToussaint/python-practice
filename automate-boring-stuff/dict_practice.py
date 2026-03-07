import sys, os, shutil

# Part 1
#1
list = [
    {"name": "potatoe", "price": 6.77, "quantity": 4},
    {"name": "hand_sanitizer", "price": 2.99, "quantity": 2},
    {"name": "pasta", "price": 8.77, "quantity": 2},
    {"name": "ketchup", "price": 2.00, "quantity": 1}
]

for item in list:
    if item['price'] > 5:
        print(f"{item['name']}: {item['price']}$")
    
#2
total = 0
for item in list:
    total += item['price'] * item['quantity']
print(f"total: {total}")

# Part 3
#2.1
students = {
    "Alice": {
        "math": 85,
        "science": 92,
        "english": 78
    },
    "Bob": {
        "math": 70,
        "science": 65,
        "english": 90
    },
    "Clara": {
        "math": 95,
        "science": 88,
        "english": 91
    }
}
all_average = {}
for name, grades in students.items():
    total = 0
    count = 0
    for subject, grade in grades.items():
        total += grade
        count += 1
    average = total / count
    all_average[name] = average
    print(f"{name} moyenne = {average:.2f}")

#best_student = max(all_average, key=all_average.get)
#best_average = all_average[best_student]
best_student = None
best_average = 0
for name, average in all_average.items():
    if average > best_average:
        best_average = average
        best_student = name

print(f"the best student is {best_student}, average: {best_average}")

# 2.2 - for each subject, find the higher average and the name of the student
subjects = ["math", "science", "english"]

for subject in subjects:
    best_student = None
    highest = 0

    for name, grades in students.items():
        if grades[subject] > highest:
            highest = grades[subject]
            best_student = name
    
    print(f"{subject}: {best_student}({highest})")

# Part 4 - default
# 4.1 get the info in this format {mois: {produit: quantité}}
sales = [
    ("Janvier", "Pommes", 150),
    ("Janvier", "Bananes", 200),
    ("Février", "Pommes", 180),
    ("Février", "Bananes", 160),
    ("Février", "Oranges", 90),
    ("Mars", "Pommes", 200),
    ("Mars", "Bananes", 220),
]

results = {}
for month, article, quantity in sales:
    results.setdefault(month, {})
    results[month][article] = quantity
print(results)

for month, products in results.items():
    total = 0
    for product, quantity in products.items():
        total += quantity
    print(f"{month}: {total}")

# Part 5 - dict as parameter
# 5.1 - J'ai pas trop bien compris quoi faire
def create_student(name, math, science, english):
    return {
        "name": name,
        "math": math,
        "science": science,
        "english": english
    }

def print_report(student):
    print(f"""
            name: {student["name"]}
            math: {student["math"]}
            science: {student["science"]}
            english: {student["english"]}
          """)

print_report(create_student("Hans", 78, 90, 63))

# Part 6 - config
#6.1
CONFIG = {
    "images": {
        "extensions": [".jpg", ".png", ".gif"],
        "folder": "Images"
    },
    "documents": {
        "extensions": [".pdf", ".docx", ".txt"],
        "folder": "Documents"
    },
    "music": {
        "extensions": [".mp3", ".wav"],
        "folder": "Musique"
    }
}

if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    print("Needed the folder path")
    sys.exit()

summary = {}

for category, config in CONFIG.items():
    summary[category] = 0

for filename in os.listdir(folder):
    ext = os.path.splitext(filename)[1].lower() # -> ".jpg", ".pdf", etc.

    copied = False
    for category, config in CONFIG.items():
        if ext in config["extensions"]:
            dest = os.path.join(folder, config["folder"])
            os.makedirs(dest, exist_ok=True)
            shutil.copy(os.path.join(folder, filename), dest)
            summary[category] += 1
            copied = True
            break

    if not copied:
        summary.setdefault("non_classe", 0)
        summary["non_classe"] += 1
