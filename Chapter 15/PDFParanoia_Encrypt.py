#! Python3
# PDFParanoia_Encrypt.py - Encrypts all pdfs in a user defined folder and all subfolders

import os, PyPDF2, pyinputplus
from pathlib import Path

def main():
    directory = Path(input('Enter the full path of the directory to encrypt(use forward slashes): '))
    while True:
        password = pyinputplus.inputPassword('Enter a password for the encrypted PDF files: ')
        if pyinputplus.inputPassword('Enter the password again: ') != password:
            print('Passwords were different, try again')
        else:
            break
    encryptPDFs(str(directory), password)

def encryptPDFs(directory, password):
    for folderName, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            # Find each pdf file
            if filename.endswith('.pdf'):
                pdfWriter = PyPDF2.PdfFileWriter()
                pdfFileObj = open(os.path.join(folderName, filename), 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                # Go through each page in the pdf
                for pageNumber in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNumber)
                    pdfWriter.addPage(pageObj)
                # Determine the name of the file
                newFileName = filename[:-4] + '_encrypted.pdf'
                # Save the pdf
                newFile = open(os.path.join(folderName, newFileName), 'wb')
                pdfWriter.encrypt(password)
                pdfWriter.write(newFile)
                newFile.close()
                pdfFileObj.close()
                # Delete the unencrypted file
                os.unlink(os.path.join(folderName, filename))


if __name__ == '__main__':
    main()