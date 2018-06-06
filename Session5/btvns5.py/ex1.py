inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# gold = inventory["gold"]
# print(gold)

inventory['pocket'] = ['seashell', 'strange berry','lint']

# for key , val in inventory.items():
#     print(key , val)

for k in inventory:
    if k == 'backpack':
        inventory[k].remove('dagger')

# for key , val in inventory.items():
#     print(key , val)

inventory['gold'] = 50

for key , val in inventory.items():
    print(key , val)