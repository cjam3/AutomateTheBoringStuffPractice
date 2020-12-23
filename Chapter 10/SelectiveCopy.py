#! Python 3
# SelectiveCopy.py - Copies files of a certain extension to a folder

from pathlib import Path
import os, shutil

def main():
    SelectiveCopy()

def SelectiveCopy():
    # Copies specific files in the current working directory to a directory defined by the user
    # If the path specified does not exist the user has the option of creating it
    # Otherwise the program ends and no files are copied
    cwd = Path.cwd()
    files = cwd.glob('*.pdf')
    strDestination = input('Enter the path of the destination folder(using forward slashes): ')
    Destination = Path(strDestination)

    if not Destination.exists():
        if input('Path could not be found. Would you like to create it?[y/n]: ').lower() == 'y':
            os.makedirs(str(Destination))
        else:
            print('No files copied.')
            return
    
    for file in files:
        shutil.copy(file, Destination)
        
    print(f'Files copied to {str(Destination)}!')


if __name__ == '__main__':
    main()