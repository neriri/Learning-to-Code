stuff = {'Rope': 1, 'Torch': 6, 'Gold coin': 42, 'Dagger':1, 'Arrow':12}

def displayInventory(inventory):

    print('Inventory')
    item_total = 0
    for k, v in inventory.items():
        print(k+': ' + str(v))
        item_total += v
    print('Total number of items: '+ str(item_total))

displayInventory(stuff)
