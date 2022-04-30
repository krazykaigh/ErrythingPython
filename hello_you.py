# Ask user for name
from types import CoroutineType


name = input("What is your name? ")
print(f"{name} is a very nice name!")
# Ask user for age
age = input (f"{name} what is your age? ")
print(f"Well, {name}, it's nice to know that you are {age} years old.")

# Ask user for city
city = input(f"Tell me {name}, what city do you live in? ")
print(f"Let's see if I got this right. Your name is {name}. Your age is {age}, and you live in the city of {city}.")

# Ask user for what they enjoy
enjoyment = input(f"{name}, please tell me what you like to do? ")
print(f"{name}, I like to {enjoyment}, too.")

# Create output text

print(f"This is the information I collected: \nYour name is {name}.")
print(f"Your age is {age}.")
print(f"You live in the city of {city}.")
print(f"You like to {enjoyment}.")

# Print output to screen