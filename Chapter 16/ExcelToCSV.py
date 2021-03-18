#! python3
# ExcelToCSV.py - Converts all excel spreadsheets in the working directory to CSV files

import csv, openpyxl, os

def main():
    ExcelToCSV()

def ExcelToCSV():
    for excelFile in os.listdir('.'):
        # Skip non-xlsx files
        if not excelFile.endswith('.xlsx'):
            continue
        
        wb = openpyxl.load_workbook(excelFile)
        # Loop through each sheet
        for sheetName in wb.sheetnames:
            # Load sheet
            sheet = wb[sheetName]

            # Create csv file and writer
            fileName = excelFile[:-5] + '_' + sheetName + '.csv'
            csvFile = open(fileName, 'w', newline='')
            csvWriter = csv.writer(csvFile)

            # Loop through the rows in the spreadsheet
            for rowNum in range(1, sheet.max_row):
                rowData = []
                for colNum in range(1, sheet.max_column):
                    rowData.append(sheet.cell(row = rowNum, column = colNum).value)
                
                # Write list to csv file
                csvWriter.writerow(rowData)
            
            csvFile.close()


if __name__ == '__main__':
    main()