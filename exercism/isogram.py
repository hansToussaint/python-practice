"""This function determines if the passed in string is an heterogram"""

def is_isogram(string):
    """
    Determine if a word or phrase is an isogram.
    Args:
        string (str): The word or phrase to check.
    Returns:
        bool: True if it's an isogram, False otherwise.
    """
    
    # Clean up the string to remove spaces and tiret and Convert to lowercase first
    cleaned = [char.lower() for char in string if char.isalpha()]

    # Create a set
    set_string = set(cleaned)

    # Compare the set with the cleaned string and return the value
    return len(set_string) == len(cleaned)
        

# Other solution
"""
 def is_isogram(string):
    string = string.lower()
    
    cleaned_string = []
    for char in string:
        if char.isalpha():
            cleaned_string.append(char)

    # cleaned_string = ''.join(char for char in string if char.isalpha()) #return str
    
    for char in cleaned_string:
        if cleaned_string.count(char) > 1:
            return False

    return True
"""