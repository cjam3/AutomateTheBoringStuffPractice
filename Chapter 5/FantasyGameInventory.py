def main():
    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventroy(inventory)

def displayInventroy(inventory):
    print("Inventory:")
    itemTotal = 0
    for key, value in inventory.items():
        print(str(value) + " " + key)
        itemTotal += value

    print("Total number of items: " + str(itemTotal))

if __name__ == '__main__':
    main()