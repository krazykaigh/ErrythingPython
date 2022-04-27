import random

health =  50

potion_health = random.randint(25, 50)
print('Potion health = {}'.format(potion_health))

health += potion_health

print('Health after picking up potion = l{}'.format(health))