#! Python3
# PDFParanoia_Decrypt.py - Finds every pdf file in a directory and subdirectory and creates a decrypted copy of the file

import os, PyPDF2, pyinputplus
from pathlib import Path

def main():
    directory = Path(input('Enter the full path of the directory to encrypt(use forward slashes): '))
    while True:
        password = pyinputplus.inputPassword('Enter the password for the encrypted PDF files: ')
        if pyinputplus.inputPassword('Enter the password again: ') != password:
            print('Passwords were different, try again')
        else:
            break
    decryptPDFs(str(directory), password)

def decryptPDFs(directory, password):
    for folderName, subfolders, filenames in os.walk(directory):
        # Find each pdf
        for filename in filenames:
            if filename.endswith('.pdf'):
                pdfFileObj = open(os.path.join(folderName, filename), 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                # If the file is not encrypted then pass on the file
                if not pdfReader.isEncrypted:
                    pdfFileObj.close()
                    continue
                # Decrypt the file
                if pdfReader.decrypt(password) == 0:
                    print(f'Wrong password for {filename}!')
                    print('Skipping...')
                    pdfFileObj.close()
                    continue
                # Create new pdf
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNumber in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNumber)
                    pdfWriter.addPage(pageObj)
                # Determine file name
                newFileName = filename[:-4] + '_copy.pdf'
                newFile = open(os.path.join(folderName, newFileName), 'wb')
                pdfWriter.write(newFile)
                newFile.close()
                pdfFileObj.close()

                


if __name__ == '__main__':
    main()