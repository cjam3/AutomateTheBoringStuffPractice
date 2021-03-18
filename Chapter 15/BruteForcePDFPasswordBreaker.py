#! Python3
# BruteForcePasswordBreaker.py - Tries to decrypt an encrypted pdf file by using 44,000 english words
# Use --> python3 BruteForcePDFPasswordBreaker.py (name of pdf)

import PyPDF2, sys

def main():
    if len(sys.argv) != 2:
        print('Invalid number of arguments')
        print('Use --> python3 BruteForcePDFPasswordBreaker.py (name of pdf)')
        exit(0)

    BreakPassword(sys.argv[1])

def BreakPassword(fileName):
    # Create a list of all dictionary words
    dictionaryFile = open('dictionary.txt', 'r')
    dictionary = dictionaryFile.readlines()
    dictionaryFile.close()

    # Open pdf
    pdfFile = open(fileName, 'rb')
    pdfFileReader = PyPDF2.PdfFileReader(pdfFile)

    if not pdfFileReader.isEncrypted:
        print('The PDF provided is not encrypted')
        return

    # Try to decrypt pdf file
    for word in dictionary:
        if pdfFileReader.decrypt(word.strip()) == 1:
            print('Password found!')
            print(f'The password is {word.strip()}')
            pdfFile.close()
            return
        if pdfFileReader.decrypt(word.strip().lower()) == 1:
            print('Password found!')
            print(f'The password is {word.strip().lower()}')
            pdfFile.close()
            return
    

if __name__ == '__main__':
    main()