import copy


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)


def printTable(table):
    colWidths = [0] * len(table)

    for i in range(len(table)):
        longest = 0
        for j in range(len(table[i])):
            if len(table[i][j]) > longest:
                longest = len(table[i][j])
        colWidths[i] = longest

    padList = [""] * len(table[0])
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j].rjust(colWidths[i])
            if len(padList[j]) == 0:
                padList[j] = table[i][j]
            else:
                padList[j] = padList[j] + " " + table[i][j]

    print('\n'.join(padList))


if __name__ == '__main__':
    main()
