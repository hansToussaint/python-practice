#! python3
# delete_unneeded_files.py - Walks through a folder tree and searches for
# exceptionally large files or folders. Print this files

import os

def delete_unneeded_files(folder, size):
    #Walks through the folder
    number = 1
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            file_size = os.path.getsize(filepath)
            if file_size >= size:
                print(f'{number}. {filepath} - {file_size} bytes')
                number += 1

    print('Done')

#desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
#delete_unneeded_files(os.path.join(desktop, 'delicious'), 10)
