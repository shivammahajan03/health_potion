# How to increase the health of a player after the use of Health Potion?

# Health potion will increase the health with a random number anywhere between 25 and 50
# We'll be using Random module for this
# Introducing the difficulty level for different values of health potion

import random # Importing the module

health = 50  #health at the start of the game

#Assigning difficulty as Easy = 1, Medium = 2, Difficulty = 3
difficulty = random.randint(1, 3)

# Dividing by difficulty level would make sure at higher difficulty, potion_health is less

potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health

print("Difficulty - ", difficulty)
print("Health increased to - ", health)
