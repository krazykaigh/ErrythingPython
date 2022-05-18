known_users = ['Alice', 'Blobert', 'Zeral', 'Keerub', 'Myrr-Terenial', 'Kai']
low_known_users = known_users.copy()

#print(f'known_users = {known_users}')

while True:
    print('Hi! My name is Travis')
    name = input("What is your name?: ").strip()
 
    lowName = name.lower()
 
    for i in range (len(known_users)):
            low_known_users[i] = low_known_users[i].lower()
    #        
    print(f'known_users after Lower()= {known_users}')

    if (lowName in low_known_users ):
        placeIndex = low_known_users.index(lowName)    
        #
        print(f'placeIndex = {placeIndex}')

        print(f'Hello, {known_users[placeIndex]}')
        remove = input('Would you like to be removed from the system (y/n)?: ').strip().lower()
        print(f"remove = {remove}")
        if remove == 'y':
            print(f'{known_users[placeIndex]} you will be deleted from my list.')
            del(known_users[placeIndex])
            print(f'known_users = {known_users}')
            low_known_users = known_users.copy()
        elif remove == 'n':
            print('No problem, I didn\'t want you to leave anyway')

    else:
        print(f'{name} you are NOT on my list')
        add_me = input('Would you like to be added to my systems authorized user\'s list (y/n)?:').strip().lower()
        if add_me == 'y':
            print(f'{add_me} you have been added to my list!')
            known_users.append(name)
            low_known_users = known_users.copy()

        elif add_me =='n':
            print('No worries, thank you for visiting!');    
