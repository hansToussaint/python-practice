#This is  practice exercism in the chapter about dictionaries
#Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0

    for k, v in inventory.items():
        #FILL THIS PART IN
        #---My solution--:
        item_total = item_total + v #inventory.get(k, 0)
        
        print(str(v) + ' ' + k)

    print('Total number of items: ' + str(item_total))

display_inventory(stuff)

#List to Dictionary Function for Fantasy Game Inventory

def add_to_inventory(inventory, added_items):
    # your code goes here
    #---My solution--:
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory
    
inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)
