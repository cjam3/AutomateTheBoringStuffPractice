#! Python 3
# Program searches a directory and lists all files that are over 100MB in size

from pathlib import Path
import os

def main():
    strPath = input('Input the path of the folder you would like to search (use forward slashes to separate directories): ')
    pathToSearch = Path(strPath)
    files = findBiggestFiles(pathToSearch)
    print(files)

def findBiggestFiles(pathToSearch):
    # Parameters - pathToSearch is a Path to a directory
    # Function walks through the directory tree and adds path of files over 100MB to a list
    # Returns the list of file paths

    # Walk through directory
    filesOver100 = []
    for foldername, subfolder, filenames in os.walk(pathToSearch):
        for file in filenames:
            if os.path.getsize(os.path.join(foldername, file)) > 10**8:
                filesOver100.append(Path(os.path.join(foldername, file)))
    
    return filesOver100

if __name__ == '__main__':
    main()