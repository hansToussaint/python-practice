while True:
    print('Who are you')
    name = input()
    if name != 'Joe':
        continue
    print('Heelo, Joe. What\'s the password? (It\'s a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
