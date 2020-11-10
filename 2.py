# Rolling dice simulator

import random

roll = input("Press Y to roll the dice, press Q to quit : ")

while roll.lower() == "y":
    result = random.randint(1, 6)
    print("The dice rolled and you got ", result)
    roll = input("Press Y to roll again, Q to quit : ")

print("Thank you for playing!")

