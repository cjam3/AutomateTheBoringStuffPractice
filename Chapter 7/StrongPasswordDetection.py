import re


def main():
    password = 'Potato1'
    print(detectStrongPassword(password))


def detectStrongPassword(password):
    numReg = re.compile(r'\d')
    upperReg = re.compile(r'[A-Z]')
    lowerReg = re.compile(r'[a-z]')
    numMo = numReg.search(password)
    upperMo = upperReg.search(password)
    lowerMo = lowerReg.search(password)

    if numMo == None or upperMo == None or lowerMo == None:
        return False

    return True


if __name__ == '__main__':
    main()
