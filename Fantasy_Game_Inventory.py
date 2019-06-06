inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#Function lists out items in inventory 
def displayInventory(inv):
    total = 0
    print("Inventory:")
    for item , num in inv.items():
        print(str(num) + " " + item)
        total += num
    print("Total number of items:" + str(total))
    
#Function looks to add items to inventory 
def addToInventory(inventory, addedItems):
    for items in addedItems:
        inventory.setdefault(items, 0)
        inventory[items] = inventory[items] + 1
    print(inventory)
    


test = displayInventory(inventory)        
test2 = addToInventory(inventory, dragonLoot)
