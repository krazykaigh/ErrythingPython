import random

""" Set Difficulty Level """

difficulty = random.randint(1,3)

health =  50
print('Health before picking up potion = {}'.format(health))

if difficulty == 1:
    print('Difficulty Level = Easy')
    potion_health = random.randint(25, 50)

elif difficulty == 2:
    print('Difficulty Level = Normal')
    potion_health = random.randint(15, 25)

else:
    print('Difficulty Level = Hard')
    potion_health = random.randint(5, 15)

print('Potion health = {}'.format(potion_health))

health += potion_health

print('Health after picking up potion = {}'.format(health))