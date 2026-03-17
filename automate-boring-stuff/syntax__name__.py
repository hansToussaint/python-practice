# if __name__ == "__main__": veut dire : "exécute ce bloc seulement si ce fichier est lancé directement, pas importé".

# structure standard des scripts pro python
"""
# 1. Imports
import os, sys, re

# 2. Constantes / Configuration
CONFIG = {...}

# 3. Fonctions
def func1():
    ...

def func2():
    ...

def main():
    ...

# 4. Point d'entrée
if __name__ == "__main__":
    main()
"""
# explanation of __name__ == "__main__"
"""
#1 - __name__ is a special variable that holds the name of the current module. 
When a module is run directly, __name__ is set to "__main__". 
When it is imported, __name__ is set to the module's name.

example:
# In a file called my_module.py
def my_function():
    return "Hello, World!"

if __name__ == "__main__":
    print(my_function())
# If you run my_module.py directly, it will print "Hello, World!" because __name__ == "__main__".
# If you import my_module in another file, it will not print anything because __name__ will be "my_module", not "__main__".
"""