import requests ## Requires pip install
import time
import base64
import json

print('='*24)
print('\n MineUser V0.2-B'
      'https://github.com/Ecl4ts/MineUser\n'
      'GNU AFFERO GENERAL PUBLIC LICENSE\n')
print('='*24)
def Main():
    print('\nSelect an option:'
          '\n1. Check Username Availability' # Finished
          '\n2. Username to UUID' # Finished
          '\n3. UUID to username' # Finished
          '\n4. Skin From  UUID' # Finished
          '\n5. Skin from username' # Up next (V0.3-B)
          '\n6. Cape from UUID' # Up next (V0.3-B)
          '\n7. Cape From Username' # Up next (V0.3-B)
          '\n8. Generate Username' # V0.4-B
          '\n9. Exit') # Finished
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
    elif Selection == '3':
        UUID = input('UUID:\n')
        ID = UUID
        UUID = f'https://api.minecraftservices.com/minecraft/profile/lookup/{UUID}'
        UUID = requests.get(UUID).json()
        if not 'id' in UUID:
            print('Username is free or invalid.')
        elif 'id' in UUID:
            print(f'Username for {ID} is {UUID["name"]}')
        time.sleep(4)
        Main()
    elif Selection == '4':
        UUID = input('UUID:\n')
        ID = UUID
        Skin = f'https://sessionserver.mojang.com/session/minecraft/profile/{UUID}'
        Name = f'https://api.minecraftservices.com/minecraft/profile/lookup/{UUID}'
        Skin = requests.get(Skin).json()
        Name = requests.get(Name).json()
        Name = Name['name']
        if not 'id' in Skin:
            print('Username is free or invalid.')
        elif 'id' in Skin:
            Skin = json.loads(base64.b64decode(Skin['properties'][0]['value']))['textures']['SKIN']['url']
            print(f'Skin texture link for {ID} ({Name}) is {Skin}')
            time.sleep(4)
            Main()
    elif Selection == '9':
        exit('Shut down by user.')
    elif Selection <= '8':
        print('Feature is coming soon.')
        Main()
    else:
        print('Invalid selection.')
        Main()
Main()
