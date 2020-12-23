#! Python 3
# Program fills in gaps in file names with a specific prefix
# Files must be in format (prefix)(number).txt

import os, shutil
from pathlib import Path


def main():
    prefix = 'spam'
    number = '???'
    suffix = '.txt'
    sliceBegin = -7 # Index of the start of the number in the pattern
    sliceEnd = -4 # Index of the end of the number in the pattern
    fillGaps(prefix, number, suffix, sliceBegin, sliceEnd)
    # createGap(prefix, number, suffix, sliceBegin, sliceEnd, 2)

def fillGaps(prefix, number, suffix, sliceBegin, sliceEnd):
    cwd = Path.cwd()
    files = list(cwd.glob(prefix + number + suffix)) # Pattern to recognize
    files.sort()
    numFiles = len(files)

    for i in range(numFiles):
        toStr = str(files[i])[sliceBegin:sliceEnd]
        num = int(toStr)
        if num != i + 1:
            replace = prefix + str(i + 1).zfill(len(number)) + suffix
            shutil.move(files[i], os.path.join(os.getcwd(), replace))
    
def createGap(prefix, number, suffix, sliceBegin, sliceEnd, location):
    cwd = Path.cwd()
    files = list(cwd.glob(prefix + number + suffix)) # Pattern to recognize
    files.sort(reverse=True)
    numFiles = len(files)

    for i in range(numFiles - (location - 1)):
        toStr = str(files[i])[sliceBegin:sliceEnd]
        num = int(toStr)
        replace = prefix + str(num + 1).zfill(len(number)) + suffix
        shutil.move(files[i], os.path.join(os.getcwd(), replace))

if __name__ == '__main__':
    main()
