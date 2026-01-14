import requests
import time

print('='*24)
print('\n MineUser V0.1-B'
      'https://github.com/Ecl4ts/MineUser\n'
      'GNU AFFERO GENERAL PUBLIC LICENSE\n')
print('='*24)
def Main():
    print('\nSelect an option:'
          '\n1. Check username availability'
          '\n2. Username to UUID'
          '\n3. UUID to username'
          '\n4. Skin from UUID'
          '\n5. Skin from username'
          '\n6. Cape from UUID'
          '\n7. Cape from username'
          '\n8. Generate username'
          '\n8. Exit')
    print('=' * 24)

    Selection = input('Option:\n')
    if Selection == '1':
        Username = input('Username:\n')
        Username = f'https://api.mojang.com/minecraft/profile/lookup/name/{Username}'
        Username = requests.get(Username).json()
        if not 'id' in Username:
            print('Username is free or invalid.')
        elif 'id' in Username:
            print(f'Username is taken. (ID: {Username["id"]})')

        time.sleep(4)
        Main()
    elif Selection == '2':
        Username = input('Username:\n')
        User = Username
        Username = f'https://api.mojang.com/minecraft/profile/lookup/name/{Username}'
        Username = requests.get(Username).json()
        if not 'id' in Username:
            print('Username is free or invalid.')
        elif 'id' in Username:
            print(f'UUID for {User} is {Username["id"]}')
        time.sleep(4)
        Main()
    elif Selection == '8':
        exit('Shut down by user.')
    elif Selection <= '8':
        print('Feature is coming soon.')
        Main()
    else:
        print('Invalid selection.')
        Main()
Main()
