import random # Importing the module

health = 50  # health at the start of the game

#Assigning difficulty as Easy = 1, Medium = 2, Difficulty = 3
difficulty = random.randint(1, 3)

# Dividing by difficulty level would make sure at higher difficulty, potion_health is less

potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health

print("Difficulty - ", difficulty)
print("Health increased to - ", health)
