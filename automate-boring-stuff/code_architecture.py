#2 - return function
#2.1 - create a function that find the largest file's size using os.walk

import os, sys

def find_largest_file(folder):
    folder_info = {}
    largest_file = None
    largest_size = 0
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)

            if size > largest_size:
                largest_size = size
                largest_file = {
                    "name": file,
                    "path": full_path,
                    "size": size
                }
    return largest_file

#3 return tuple
#3.1 write a function that verify args form command line
# - as least 1 argument, verify that the folder exist, verify that it is a folder
# - return (True, folder_path) or (False, error_message)

def validate_args():
    if len(sys.argv) < 2:
        return False, f"please type at least 1 argument to continue (folder path)"

    folder = sys.argv[1]    
    
    if not os.path.exists(folder):
        return False, f"Folder '{folder}' not found"
    if not os.path.isdir(folder):
        return False, f"'{folder}' is not a valid folder"
    return True, folder
