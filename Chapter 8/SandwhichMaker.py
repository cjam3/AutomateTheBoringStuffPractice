import pyinputplus as pyip 

def main():
    sandwhichMaker()

def sandwhichMaker():
    breadCosts = {'white' : 1, 'wheat' : 2, 'sourdough': 3}
    proteinCosts = {'chicken' : 2, 'turkey' : 2, 'ham' : 3, 'tofu' : 2}
    cheeseCosts = {'cheddar' : 2, 'swiss' : 3, 'mozzarella' : 3}

    sandwhichCost = 0
    bread = pyip.inputMenu(['white', 'wheat', 'sourdough'])
    sandwhichCost += breadCosts[bread]

    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
    sandwhichCost += proteinCosts[protein]

    wantCheese = pyip.inputYesNo('Would you like cheese: ')
    if wantCheese == 'yes':
        cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
        sandwhichCost += cheeseCosts[cheese]
    
    mayo = pyip.inputYesNo('Would you like mayo?: ')
    mustard = pyip.inputYesNo('Would you like mustard?: ')
    lettuce = pyip.inputYesNo('Would you like lettuce?: ')
    tomato = pyip.inputYesNo('Would you like tomato?: ')

    numberOfSandwhiches = pyip.inputInt('How many sandwhiches would you like?: ', min = 1)

    print('The total cost of your order is: $%s' % (numberOfSandwhiches * sandwhichCost))


if __name__ == '__main__':
    main()