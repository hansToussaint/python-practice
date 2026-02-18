#! python3
# selective_copy.py - Walks trough a folder tree and searches for files
# with a certain extension (such as .pdf or .jpg)
# Copy this files from whatever location they are in to a new folder

import os, shutil

def selective_copy(folder, extension):
    # Make sure the folder is absolute
    folder = os.path.abspath(folder)

    #rename the folder with the same name + _copy(extension)_X
    number = 1
    while True:
        folder_name = folder + '_copy(' + extension + ')' + '_' + str(number)

        if not os.path.exists(folder_name):
            break
        number += 1
        
    # Create a new folder in the same location with a correct name
    os.makedirs(folder_name)
    
    # Walks through the folder
    for foldername, subfolders, filenames in os.walk(folder):
        # Find files with the extension
        for filename in filenames:
            if filename.endswith(extension):
                # copy each file from the location to a new folder
                file = os.path.join(foldername, filename)
                print(f'Copying {file} to {folder_name}')
                shutil.copy(file, folder_name)
                
    print('Done')

#desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
#selective_copy(os.path.join(desktop, 'delicious'), '.txt')
