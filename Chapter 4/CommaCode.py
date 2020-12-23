def commaList(spam):

    commaListStr = ''
    if len(spam) == 0:
        return commaListStr

    for index, item in enumerate(spam):
        if index == len(spam) - 1:
            commaListStr = commaListStr + 'and ' + str(item)
        else:
            commaListStr = commaListStr + str(item) + ', '
    return commaListStr


def main():
    spam = ['apples', 'bananas', 4, 'cats']
    print(commaList(spam))


if __name__ == '__main__':
    main()
