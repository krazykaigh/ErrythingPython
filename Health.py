import random

health =  50
print('Health before picking up potion = {}'.format(health))

potion_health = random.randint(25, 50)
print('Potion health = {}'.format(potion_health))

health += potion_health

print('Health after picking up potion = {}'.format(health))