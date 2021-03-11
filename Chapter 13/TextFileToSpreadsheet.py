#! Python3
# TextFileToSpreadsheet.py - Reads multiple text files and writes the lines to a spreadsheet
# Each column represents an individual text file and row represents a line
# Use --> python3 TextFileToSpreadsheet.py (x number of filenames)

import openpyxl, sys, os

def main():
    if len(sys.argv) < 2:
        print('Invalid number of arguments')
        print('Use --> python3 TextFileToSpreadsheet.py (x number of filenames)')
        exit(0)

    TextFileToSpreadsheet(sys.argv[1:])

def TextFileToSpreadsheet(fileNames):
    wb = openpyxl.Workbook()
    sheet = wb.active
    fileNumber = 1
    for fileName in fileNames:
        # Open file and readlines
        textFile = open(fileName, 'r')
        lines = textFile.readlines()
        # Save each line to a row in a column in a spreadsheet
        for i in range(len(lines)):
            sheet.cell(row = i + 1, column = fileNumber).value = lines[i].strip('\n')
        textFile.close()
        fileNumber += 1
    wb.save('TextFileToSpreadsheet.xlsx')


if __name__ == '__main__':
    main()