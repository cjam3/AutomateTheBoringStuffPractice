import random


def main():
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        randList = generateRandomList()
        numberOfStreaks += findStreak(randList)
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))


def findStreak(randList):
    state = 0
    for i in range(1, len(randList)):
        if(randList[i - 1] == randList[i]):
            state += 1
        else:
            state = 0
        if state == 5:
            return 1

    return 0


def generateRandomList():
    randList = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            randList.append('H')
        else:
            randList.append('T')

    return randList


if __name__ == '__main__':
    main()
