# Guessing a random number

import random

num = random.randint(1, 100)
print("I've chosen a random number between 1 and 100.")

while True:
    result = input("Guess the number : ")
    i = int(result)
    if i == num:
        print("You guessed it right!")
        break
    elif i < num:
        print("The number is greater than you guessed")
    elif i > num:
        print("The number is lower than you guessed")
