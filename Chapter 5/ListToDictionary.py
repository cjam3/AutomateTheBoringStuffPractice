def main():
    inv = {'gold coin': 42, 'rope': 1}
    displayInventroy(inv)
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventroy(inv)


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def displayInventroy(inventory):
    print("Inventory:")
    itemTotal = 0
    for key, value in inventory.items():
        print(str(value) + " " + key)
        itemTotal += value

    print("Total number of items: " + str(itemTotal))

if __name__ == "__main__":
    main()
